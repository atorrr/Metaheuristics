import numpy as np
import copy
import random as rd
import gen_al_def as genf
import time
import matplotlib.pyplot as plt
import TestFunctions as tf


#%% hyperparameters
prob_crsvr      = 1
prob_mute       = 0.3
N               = 200    #population size
generations     = 180

#%%decision variables encoding
chromosome = np.array([1,0,0,1,1,0,0,1,1,0,0,1,0,0,
                       0,1,1,0,1,0,1,0,1,1,0,0,1,1]) #x_y string
    

all_solutions       = np.empty((0, len(chromosome)))

best_of_generation  = np.empty((0,len(chromosome)+1))

#function to optimize
fun=tf.Schaffer2

#%% initial pop 
for i in range(N):
    rd.shuffle(chromosome) #shuffle
    all_solutions   =   np.vstack((all_solutions, chromosome))

start_time  =   time.time()
gen         =    1

for i in range(generations):
    new_pop     = np.empty((0,len(chromosome)))
    new_pop_ov  = np.empty((0,len(chromosome)+1))
    sorted_best = np.empty((0,len(chromosome)+1)) #for plotting
    
    family      = 1     #tracking purposes
    
    for j in range(int(N/2)): #each time we have 2 childrens
        #find parents
        boomers     = genf.find_parents(all_solutions)
        parent_1= boomers[0]
        parent_2= boomers[1]
        #make childrens
        new_generation=genf.crossover(parent_1,parent_2)
        #mutate childrens
        ng_originals        = copy.deepcopy(new_generation)
        new_generation_mutes= genf.muta(new_generation)
        milenial_1          = new_generation_mutes[0]
        milenial_2          = new_generation_mutes[1]
        #evaluate the children
        ov_milenial_1       = genf.ov_fun(milenial_1,fun)[2]
        ov_milenial_2       = genf.ov_fun(milenial_2,fun)[2]
        #all in one vector
        milenial_1_ov       = np.hstack((ov_milenial_1, milenial_1))
        milenial_2_ov       = np.hstack((ov_milenial_2, milenial_2))
        #new population for the next generation
        new_pop             = np.vstack((new_pop, milenial_1, milenial_2))
        new_pop_ov          = np.vstack((new_pop_ov, milenial_1_ov, milenial_2_ov))
        
        family += 1
    #now my new pop is my initial one    
    all_solutions       = new_pop
    sorted_best         = np.array(sorted(new_pop_ov, key=lambda x:x[0])) #for plotting
    best_of_generation  = np.vstack((best_of_generation, sorted_best[0])) #for plotting
    
    gen += 1

end_time = time.time() #timing purposes

sorted_last_pop     = np.array((sorted(new_pop_ov, key=lambda x:x[0])))
sorted_best_of_gen  = np.array((sorted(best_of_generation, key=lambda x:x[0])))

#the best
best_str_convergence = sorted_last_pop[0]
best_str_overall     = sorted_best_of_gen[0]

#%% Printing my solutions
print("Convergence")
print("\n Final Solution (best)", best_str_convergence[1:])
print("\n Best value", best_str_convergence[0])
print("\n Encoded X (best)", best_str_convergence[1:int(len(chromosome)/2)])
print("\n Encoded Y (best)", best_str_convergence[int(len(chromosome)/2):])

print("Best")
print("Final Solution (best)", best_str_overall[1:])
print("Best value", best_str_overall[0])
print("\n Encoded X (best)", best_str_overall[1:int(len(chromosome)/2)])
print("\n Encoded Y (best)", best_str_overall[int(len(chromosome)/2):])

#time details

print("\n Execution time:", round(end_time - start_time,2), " seconds")

final_sol_convergence   = genf.ov_fun(best_str_convergence[1:],fun)
final_sol_overall       = genf.ov_fun(best_str_overall[1:],fun)

print("\n Final solution convergence \n x:",round(final_sol_overall[0],3), "\n y:",round(final_sol_overall[1],3), "\n z:",round(final_sol_overall[2],3), )

#%% Plotting my best solution for each generation

best_ov_convergence = (best_str_convergence[0])
best_ov_overall     = best_str_overall[0]

plt.plot(best_of_generation[:,0], color='g')
bcon=plt.axhline(y=best_ov_convergence, color='r', linestyle='--')
bov=plt.axhline(y=best_ov_overall, color='y', linestyle='--')

plt.title("Z Reached Through Generations", fontsize=20)
plt.xlabel("Generation", fontsize=18)
plt.ylabel("Z",fontsize=18, fontweight='bold')
#plt.legend(bcon, ['Solution \n %s ' %best_ov_convergence], numpoints=1, loc='upper left', )
plt.legend((bcon, bov), ('Best of last generation z= %0.3f' %best_ov_convergence, 'Best Overall z= %0.3f' %best_ov_overall))

plt.show()

#plotting the function and the minimal point found
tf.PlotFun(fun,fx=final_sol_overall[0],fy=final_sol_overall[1],fz=final_sol_overall[2])


"""
if sorted_best_of_gen[-1][0]   > 2:
    k = 0.8
elif sorted_best_of_gen[-1][0] > 1:
    k = 0.5
elif sorted_best_of_gen[-1][0] > 0.5:
    k = 0.3
elif sorted_best_of_gen[-1][0] > 0.3:
    k = 0.2
else:
    k = 0.1

xyz1=(generations/6,best_ov_convergence)
xyzz1=(generations/5.4,best_ov_convergence+k)

plt.annotate("at convergence: %0.3f" %best_ov_convergence, xy=xyz1, xytext=xyzz1,
             arrowprops=dict(facecolor='black',shrink=1,width=1,headwidth=3),
             fontsize=12)

xyz2=(generations/2.4,best_ov_overall)
xyzz2=(generations/2.2,best_ov_overall+(k/2))

plt.annotate("at overall: %0.3f" %best_ov_overall, xy=xyz2, xytext=xyzz2,
             arrowprops=dict(facecolor='black',shrink=1,width=1,headwidth=3),
             fontsize=12)
"""
