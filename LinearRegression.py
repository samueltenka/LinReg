'''.............................
   Creation 2015 by Samuel Tenka
   .............................'''
''' Locally-Weighted Polynomial Linear Regression'''

import random
from numpy.linalg import *
from numpy import *
from math import *

def get_feats(point, max_deg):
   return [1.0] + [coor**d for coor in point for d in range(1, max_deg+1)]

def make_kernel(center, beta):
   def kernel(point):
      diff = point-center
      Z2 = max(-10.0, min(10.0, beta*dot(diff, diff)))
      return exp(-Z2/2)
   return kernel
   
def make_predictor(xys, max_deg, tau=None, reg_param=0.0):
   '''Now ``make_predict" doesn't take in ``target_x",
      but instead returns ``predict" that eats ``target_x".
      If tau not specified, ``predict" does global linear regression,
      avoiding the recomputation of ``weights" for each ``target_x".'''
   print("making predictor...", "(max_deg=", max_deg,
                                ") (tau=", tau,
                                ") (reg_param=", reg_param, ")")
   xs = array([get_feats(x, max_deg) for (x, y) in xys])
   ys = array([[y] for (x, y) in xys])
   
   def compute_weights(weight_func):
      xs_t_weighted = transpose(array([x*weight_func(x) for x in xs]))
      regularizer = reg_param * identity(len(xs[0]))
      pseudo_inverse = dot(inv(regularizer + dot(xs_t_weighted, xs)), xs_t_weighted)
      return dot(pseudo_inverse, ys)
      
   if tau:
      get_weight = lambda target_x: \
                   compute_weights(make_kernel(target_x, beta=1.0/tau**2))
   else:
      weights = compute_weights(make_kernel(xs[0], beta=0.0))
      get_weight = lambda target_x: weights
   
   def predict(target_x):
      if random.random() < 1E-1:
         print('.', end='')
      target_x = array(get_feats(target_x, max_deg))
      weights = get_weight(target_x)
      return dot(transpose(weights), target_x)[0]

   return predict
      

'''
## testing:
xys = [([0.0], 1.0), ([2.0], 2.0), ([4.0], 3.0), ([6.0], 4.0)]
print("max_deg==3:\t\t 1.6 ~", make_predictor(xys, max_deg=3)([1.2])) ## --> 1.6
print("max_deg==3 w/ reg.:\t 1.6 ~", make_predictor(xys, max_deg=3, reg_param=1.0)([1.2])) ## --> 1.6
print("max_deg==4:\t\t 1.6 ~", make_predictor(xys, max_deg=4)([1.2])) ## --> not 1.6
print("max_deg==4 w/ reg.:\t 1.6 ~", make_predictor(xys, max_deg=4, reg_param=1.0)([1.2])) ## --> 1.6
'''
