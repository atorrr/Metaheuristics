import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

#%% Test functions

def Himmb(x,y):
    z = ((x**2)+y-11)**2+(x+(y**2)-7)**2
    return(z)

def sph(x,y):
    z = x**2+y**2
    return(z)

def McCor(x,y): #-1.5 < x < 4, -3 < y < 4
    z = np.sin(x+y)+(x-y)**(2) -(1.5*x)+(2.5*y)+1
    return(z)

def Beale(x,y):
    z = (1.5-x+x*y)**2+(2.25-x+x*y**2)**2+(2.625-x+x*y**3)**2
    return(z)
   
def GoldP(x,y):
    z = (1+(x+y+1)**(2)*(19-14*x+3*x**2-14*y+6*x*y+3*y**2))*(30+(2*x-3*y)**2 *
         (18-32*x+12*x**2+48*y-36*x*y+27*y**2))
    return(z)
    
def Schaffer2(x,y):
    z = 0.5 + (((np.sin(x**2-y**2))**2)-0.5)/((1 +0.001*(x**2+y**2))**2)
    return(z)

def Levi(x,y):
    z = (np.sin(3*np.pi*x))**2+((x-1)**2)*(1+(np.sin(3*np.pi*y))**2)+((y-1)**2)*(1+(np.sin(2*np.pi*y))**2)
    return(z)
    
#%% Plotting test functions
def PlotFun(f,fx=0,fy=0,fz=-1):
    print("Function", f.__name__)
    x, y    = np.linspace(-10, 10, 30), np.linspace(-10, 10, 30)
    X, Y    = np.meshgrid(x, y)
    Z       = f(X, Y)
    figi    = plt.figure()
    ax      = plt.axes(projection='3d')
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow', edgecolor='none')
    ax.set_title(f.__name__)
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.view_init(60, 35)
    #plot results
    solution_found = ax.plot([fx], [fy], [fz], markerfacecolor='y', markeredgecolor='g',
                             marker='o', markersize=5, alpha=1.0)
    fx,fy,fz=round(fx,2), round(fy,2), round(fz,2)
    coord=[(fx,fy,fz)]
    
    print(coord)
    ax.legend(solution_found, ['Solution \n %s ' %coord], numpoints=1, loc='upper left')
    

#%%
    #print(Beale(-0.19,5.68))
