import simulated_annealing as sima
import TestFunctions as tf

#%% Plotting my test functions
"""
figfunH= tf.PlotFun(tf.Himmb)
figfunS= tf.PlotFun(tf.sph)
figfunM= tf.PlotFun(tf.McCor)
figfunB= tf.PlotFun(tf.Beale)
figfunG= tf.PlotFun(tf.GoldP)
"""
#%% Testing my functions starting at the origin
"""
x,y=0.,0.

sima.SimAnn(x,y,tf.Himmb)
#f(3.0,2.0),f(-2.805118,3.131312),f(-3.779310,-3.283186),f(3.584428,-1.848126)=0.0
sima.SimAnn(x,y,tf.sph)
#f(0,0)=0
sima.SimAnn(x,y,tf.McCor)
#f(-0.54719,-1.54719)=-1.9133
sima.SimAnn(x,y,tf.Beale)
#f(3,0.5)=0
sima.SimAnn(x,y,tf.GoldP)
#f(0,-1)=3
"""
#%% My results

def CompleteSimAnn(x,y,fun):
    SA=sima.SimAnn(x,y,fun,2000,600)
    tf.PlotFun(fun,SA[0],SA[1],SA[2])
    print(SA)
    
CompleteSimAnn(0,0,tf.Beale)
