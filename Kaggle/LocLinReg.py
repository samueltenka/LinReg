'''.............................
   Creation 2015 by Samuel Tenka
   .............................'''
''' Locally-Weighted Polynomial Linear Regression'''

import random
from numpy.linalg import *
from numpy import *
from math import *

def make_kernel(center, beta):
   def kernel(point):
      diff = point-center
      Z2 = max(-10.0, min(10.0, beta*dot(diff, diff)))
      return exp(-Z2/2)
   return kernel
   
def make_maker(tau=1.0, reg_param=0.0):
   def maker(xys):
      xs = array([x for (x, y) in xys])
      ys = array([[y] for (x, y) in xys])
      def predict(target_x):
         target_x = array(target_x)
         kernel = make_kernel(target_x, 1.0/tau**2)
         
         xs_t_weighted = transpose(array([x*kernel(x) for x in xs]))
         regularizer = reg_param * identity(len(xs[0]))
         pseudo_inverse = dot(inv(regularizer + dot(xs_t_weighted, xs)), xs_t_weighted)
         weights = dot(pseudo_inverse, ys)
         
         return dot(transpose(weights), target_x)[0]
      return predict
   return maker


'''
## testing:
m = make_maker()
xys = [([1.0, 1.0], 1.0), ([2.0, 1.0], 1.0), ([2.0, 2.0], 2.0)]
p = m(xys)
print(p([1.0, 3.0])) ## --> 3.0
'''
