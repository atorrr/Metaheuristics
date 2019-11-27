import numpy as np
#import matplotlib as plt
import simulated_annealing as sima
import TestFunctions as tf

x,y=0.,0.

sima.SimAnn(x,y,tf.Himmb)
sima.SimAnn(x,y,tf.sph)
sima.SimAnn(x,y,tf.McCor)
sima.SimAnn(x,y,tf.Beale)
sima.SimAnn(x,y,tf.GoldP)

