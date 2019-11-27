import numpy as np

#%% Test functions

def Himmb(x,y):
    z= ((x**2)+y-11)**2+(x+(y**2)-7)**2
    return(z)

def sph(x,y):
    z=x**2+y**2
    return(z)

def McCor(x,y): #-1.5 < x < 4, -3 < y < 4
    z=np.sin(x+y)+(x-y)**(2) -1.5*x+2.5*y+1
    return(z)

def GoldP(x,y):
    z= (1+(x+y+1)**(2)*(19-14*x+3*x**2-14*y+6*x*y+3*y**2))*(30+(2*x-3*y)**2 * (18-32*x+12*x**2+48*y-
                                36*x*y+27*y**2))
    return(z)

def Beale(x,y):
   z=(1.5-x+x*y)**2+(2.25-x+x*y**2)**2+(2.625-x+x*y**3)
   return(z)


#%% Plotting test functions

def sph_p(x):
    n=len(x)
    y=zeros(n)
    c=.0
    for i in range(n):
        y[i]=x[i]**2
        yn=c+y[i]
        c=yn
    return(yn)

def McCor_p(x,y): #-1.5 < x < 4, -3 < y < 4
    n=len(x)
    z=zeros(n)
    for i in range(n):
        z[i]=np.sin(x[i]+y[i])+(x[i]-y[i])**(2)
        -1.5*x[i]+2.5*y[i]+1
    return(z)

def GoldP_p(x,y):
    n=len(x)
    z=zeros(n)
    for i in range(n):
        z[i]= (1+(x[i]+y[i]+1)**(2)*
               (19-14*x[i]+3*x[i]**2-14*y[i]+6*x[i]*y[i]+3*y[i]**2))*(
        30+(2*x[i]-3*y[i])**2 * (18-32*x[i]+12*x[i]**2+48*y[i]-
                                36*x[i]*y[i]+27*y[i]**2))
    return(z)

def Beale_p(x,y):
    n=len(x)
    z=zeros(n)
    for i in range(n):
        z[i]=(1.5-x[i]+x[i]*y[i])**2+(2.25-x[i]
                                     +x[i]*y[i]**2)**2
        +(2.625-x[i]+x[i]*y[i]**3)
    

