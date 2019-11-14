# Simulated annealing, metaheuristics
#############################################

import numpy as np
import matplotlib.pyplot as plt

#objective function (Himmelblau)
def Himmb(x,y):
    z= ((x**2)+y-11)**2+(x+(y**2)-7)**2
    return(z)
    
#initial solution
x = 0.
y = 0.
z = Himmb(x,y)


    
#printing starting point
print("The initial values are \n x=", x, "\n y=", y, "\n z=", z)

#hyperparameters
T0      =    1000
temp_for_plot = T0        #for plotting purposes
M       =     500         #steps to decrease T
N       =     15          #times of search in the neighborhood
alpha   =     0.85        #decreasing of the T

k       =     0.1         #reducing step size

#to plot the T and objective value reached
temp= []
obj_val =[] 


for m in range(M):      #cycle for decrease the T
    for n in range(N):  #cycle for neighborhood searches
        #for each decision variable
        
        rand_x_1 = np.random.rand() #change in x?
        rand_x_2 = np.random.rand() #by how much?
        
        if rand_x_1 >=0.5: #desicion
            step_size_x     =   k*rand_x_2
            
        else:
            step_size_x     =   -k*rand_x_2
            
        rand_y_1 = np.random.rand() #change in x?
        rand_y_2 = np.random.rand() #by how much?
        
        if rand_y_1 >=0.5: #desicion
            step_size_y     =   k*rand_y_2
            
        else:
            step_size_y     =   -k*rand_y_2
        
        "temporary variables"
        x_temp      =   x   + step_size_x
        y_temp      =   y   + step_size_y
        
        
        #will we move?
        obj_v_possible  =   Himmb(x_temp, y_temp)
        #current value
        obj_v_current   =   Himmb(x,y)
        
        formula = 1/(np.exp((obj_v_possible * obj_v_current)/T0))
        
        if obj_v_possible <= obj_v_current:
            x= x_temp
            y= y_temp
        elif np.random.rand() <= formula:
            x= x_temp
            y= y_temp
        else:
            x=x
            y=y
    
    temp.append(T0) #for plotting reasons
    obj_val.append(obj_v_current) #for plotting reasons
    
    T0 = alpha*T0
    
print("\n \n Final values \n x =", x, "\n y=", y, "\n objective value =", obj_v_current)

plt.plot(temp, obj_val)   
plt.title("Z value for Himmelblau function") 
plt.xlabel("Temperature")
plt.ylabel("Z")      

plt.xlim(temp_for_plot,0)
plt.xticks(np.arange(min(temp),max(temp),100))

plt.show()