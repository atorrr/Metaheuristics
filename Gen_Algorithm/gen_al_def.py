# Genetic Algorithm optimization for a continuous problem

import numpy as np

#objective function (Himmelblau) for testing
def fun(x,y):
    z= ((x**2)+y-11)**2+(x+(y**2)-7)**2
    return(z)

#%% testing bits
    """
    #TEST
chromosome_test     =   np.array([1,1,0,1,      #y variable
                                  0,1,1,0])     #x variable

#decoding for x
print("\n ### For variable x  ### \n")
z   =   0
t   =   1
x_bit_sum   =   0
for i in range(int(len(chromosome_test)/2)):
    print("\n index is:", t, "\n bit is", chromosome_test[-t], "\n z for: ",
          format(chromosome_test), "is ",z)
    x_bit   = chromosome_test[-t]*(2**z)
    print("\n ", format(chromosome_test[-t]),"*(2**",z,")=", x_bit)
    x_bit_sum += x_bit
    t   += 1
    z   += 1
    print("\n sum(bit*(2**z)) is", x_bit_sum)
    
#decoding for y
print("\n ### For variable y  ### \n")
z   =   0
t   =   int(1 + (len(chromosome_test)/2))
y_bit_sum   =   0
for i in range(int(len(chromosome_test)/2)):
    print("\n index is:", t, "\n bit is", chromosome_test[-t], "\n z for: ",
          format(chromosome_test), "is ",z)
    y_bit   = chromosome_test[-t]*(2**z)
    print("\n ", format(chromosome_test[-t]),"*(2**",z,")=", y_bit)
    y_bit_sum += y_bit
    t   += 1
    z   += 1
    print("\n sum(bit*(2**z)) is", y_bit_sum)
"""
#%% Calculation of the objective value function

def ov_fun(chromosome,fun=fun):
    
    lb_x, ub_x  =   -6, 6 #lower and upper bounds for x
    lb_y, ub_y  =   -6, 6 #lower and upper bounds for y
    len_x, len_y =   int(len(chromosome)/2), int(len(chromosome)/2)
    
    precission_x=   (ub_x-lb_x)/((2**len_x)-1)
    precission_y=   (ub_y-lb_y)/((2**len_y)-1)
    
    #decoding for x
    z   =   0
    t   =   1
    x_bit_sum   =   0
    for i in range(len_x):
        x_bit   = chromosome[-t]*(2**z)
        x_bit_sum += x_bit
        t   += 1
        z   += 1
    #decoding for y
    z   =   0
    t   =   1 + len_y
    y_bit_sum   =   0
    for i in range(len_y):
        y_bit   = chromosome[-t]*(2**z)
        y_bit_sum += y_bit
        t   += 1
        z   += 1

    decoded_x = (x_bit_sum*precission_x)+lb_x
    decoded_y = (y_bit_sum*precission_y)+lb_y
    
    #print("x value:", decoded_x)
    #print("y value:", decoded_y)

    ofv= fun(decoded_x, decoded_y)
    #print("z value found", ofv)
    
    return(decoded_x, decoded_y, ofv)
    
#%% decode testing

    
"""    

chromosome = np.array([1,1,0,1,1,0,0,1,1,0,0,1,
                       0,1,1,0,1,0,1,0,1,1,0,0,])
    
print("\n original chromosome", format(chromosome))
print("\n decoded x:", round((ov_fun(chromosome)[0]),3) ,
      "\n decoded y:", round((ov_fun(chromosome)[1]),3))

print("\n objective function value", round(ov_fun(chromosome)[2],3))
    
parent_1    = np.array([1,0,1,1,1,1,0,1,1,0,1,1,
                       1,1,1,1,0,0,1,1,1,1,0,0,])
print("\n original chromosome", format(parent_1))
print("\n decoded x:", round((ov_fun(parent_1)[0]),3) ,
      "\n decoded y:", round((ov_fun(parent_1)[1]),3))

print("\n objective function value", round(ov_fun(parent_1)[2],3))
"""

#%% get the parents
def find_parents(all_solutions,fun=fun):
    
    boomers   = np.empty((0, np.size(all_solutions,1)))
    #selecting 3 random possible parents

    for i in range(2):
        indices_list    =   np.random.choice(len(all_solutions),
                                             3,replace=False)
        poss_par_1, poss_par_2, poss_par_3 = all_solutions[indices_list[0]],all_solutions[indices_list[1]], all_solutions[indices_list[2]]
        #evaluating the boomers for parenthood
        ofv_par_1, ofv_par_2, ofv_par_3 = ov_fun(poss_par_1,fun)[2], ov_fun(poss_par_2,fun)[2], ov_fun(poss_par_3,fun)[2]
        # let's tournament begin!
        min_obj_fun = min(ofv_par_1, ofv_par_2, ofv_par_3)
        if min_obj_fun == ofv_par_1:
            selected_par = poss_par_1
        elif min_obj_fun == ofv_par_2:
                selected_par = poss_par_2
        else:
            selected_par = poss_par_3
       
        boomers= np.vstack((boomers, selected_par))
        
    parent1=boomers[0,:]
    parent2=boomers[1,:]
        
    return(parent1, parent2) 


    """ TESTING PARENTS SEARCH
parents = find_parents(all_solutions)

print("parent 1", parents[1])
 """



#%% crossover of two parents

def crossover(parent_1, parent_2,prob_crsvr=1):
    child_1     = np.empty((0,(len(parent_1))))
    child_2     = np.empty((0,len(parent_2)))
    
    rand_crsvr  = np.random.rand()      #crossover or not
    
    if rand_crsvr < prob_crsvr:
            index_1 = np.random.randint(0, len(parent_1))
            index_2 = np.random.randint(0, len(parent_2))
        
            #two point crossover method
            while index_1 == index_2:
                index_2 = np.random.randint(0, len(parent_1))
            
            if index_1 < index_2:
                # for parent 1
                seg1_par_1 = parent_1[:index_1]
                #print("seg 1 parent 1",seg1_par_1)
                seg2_par_1 = parent_1[index_1: index_2+1]
                #print("seg 2 parent 1",seg2_par_1)
                seg3_par_1 = parent_1[index_2+1:]
                #print("seg 3 parent 1",seg3_par_1)
                #for parent 2
                seg1_par_2 = parent_2[:index_1]
                #print("seg 1 parent 2",seg1_par_2)
                seg2_par_2 = parent_2[index_1: index_2+1]
                #print("seg 2 parent 2",seg2_par_2)
                seg3_par_2 = parent_2[index_2+1:]
                #print("seg 3 parent 2", seg3_par_2)
                #aber cojan
                child_1     = np.concatenate((seg1_par_1, seg2_par_2, seg3_par_1))
                child_2     = np.concatenate((seg1_par_2, seg2_par_1, seg3_par_2))
                #print("childs here", child_1, "\n", child_2)
            else:
                seg1_par_1 = parent_1[:index_2]
                seg2_par_1 = parent_1[index_2: index_1+1]
                seg3_par_1 = parent_1[index_1+1:]
                #for parent 2
                seg1_par_2 = parent_2[:index_2]
                seg2_par_2 = parent_2[index_2: index_1+1]
                seg3_par_2 = parent_2[index_1+1:]
                #aber cojan
                child_1     = np.concatenate((seg1_par_1, seg2_par_2, seg3_par_1))
                child_2     = np.concatenate((seg1_par_2, seg2_par_1, seg3_par_2))
                #print("childs here", child_1, "\n", child_2)
            
    else:
        child_1=parent_1
        child_2=parent_2
        #print("no crossover")
            
    return(child_1, child_2)
#%% testing crossover
"""
#test crossover
tp=[1,2,3,4,5]
tp2=[6,7,8,9,0]
children = crossover(tp, tp2)

print("\n child 1", children[0], "\n child 2", children[1])

"""
#%% mutations
#flip bit mutation

#mutating the two childrens

def muta(children, prob_muta=0.2):
    mutes_babies = np.empty((0, np.size(children,1)))
    mute_1     = np.empty((0,len(children[0])))
    
    for j in range(len(children)):
        #print("len children",len(children))
        child_1=children[j]
        #print("child to mutate", child_1)
        mute_child_1=np.empty((0,len(child_1)))
        #print("muted initial",mute_child_1)
        mutated_indices=[]
        t=0
        
        for i in range(len(child_1)):
            rand_mute=np.random.rand() #to mutate or not
            if rand_mute < prob_muta:
                mutated_indices.append(t)
                if child_1[t]==0:
                    child_1[t]=1
                else:
                    child_1[t]=0
                mute_child_1= child_1
                t+=1
            else:
                #print("no mutation")
                mute_child_1= child_1
                t+=1
            #print("new child:", mute_child_1)
            
        mutes_babies= np.vstack((mutes_babies, mute_child_1))
        
    mute_1=mutes_babies[0,:]
    mute_2=mutes_babies[1,:]
    #print("mutes", mutes_babies)
        
    return(mute_1,mute_2)
            
#%% Testing the mute
"""
adop_childrens=([0,0,0,0,0,0,0],[1,1,1,1,1,1,1] )  
adop_originals=copy.deepcopy(adop_childrens)   
mute_adop=muta(adop_childrens,0.5)        
    
   """ 
   #%% Decoding single chromosome

def decode(chromosome):
    
    lb_x, ub_x  =   -6, 6 #lower and upper bounds for x
    lb_y, ub_y  =   -6, 6 #lower and upper bounds for y
    len_x, len_y =   int(len(chromosome)/2), int(len(chromosome)/2)
    
    precission_x=   (ub_x-lb_x)/((2**len_x)-1)
    precission_y=   (ub_y-lb_y)/((2**len_y)-1)
    
    #decoding for x
    z   =   0
    t   =   1
    x_bit_sum   =   0
    for i in range(len_x):
        x_bit   = chromosome[-t]*(2**z)
        x_bit_sum += x_bit
        t   += 1
        z   += 1
    #decoding for y
    z   =   0
    t   =   1 + len_y
    y_bit_sum   =   0
    for i in range(len_y):
        y_bit   = chromosome[-t]*(2**z)
        y_bit_sum += y_bit
        t   += 1
        z   += 1

    decoded_x = (x_bit_sum*precission_x)+lb_x
    decoded_y = (y_bit_sum*precission_y)+lb_y
    
    #print("x value:", decoded_x)
    #print("y value:", decoded_y)
    
    return(decoded_x,decoded_y)



    
 
 
 


    



    


