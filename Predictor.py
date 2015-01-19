'''.............................
   Creation 2015 by Samuel Tenka
   .............................'''
''' Locally-Weighted Polynomial Linear Regression'''

from numpy.linalg import *
from numpy import *
from math import *

def closeness(point, center, tau):
   diff = point-center
   mag_diff = dot(diff, diff)[0][0]
   return exp(-mag_diff/(2*tau))

def get_feats(point, max_deg):
   return [1] + [coor**d for coor in point for d in range(1, max_deg+1)]
   
def predict(xys, target_x, tau=1000.0, max_deg=3):
   '''e.g.  if xys==[([0.0], 1.0), ([2.0], 2.0), ([4.0], 3.0), ([6.0], 4.0)]
      and target_x==[1.2], then should return (1.2, 1.6);
	  tau controls duration of context; if tau is small, it'll guess based
      on closest datapoints, at risk of overfitting; if tau is large, it'll
      take into account the whole history, at risk of oversimplifying.'''
   ## everybody's a 2d array, even vectors and scalars (e.g. see return)
   target_x = array([[feat] for feat in get_feats(target_x, max_deg)])
   xs = array([get_feats(x, max_deg) for (x, y) in xys])
   ys = array([[y] for (x, y) in xys])
   
   weight_func = lambda x: closeness(x, target_x, tau)
   xs_t_weighted = transpose(array([x*weight_func(x) for x in  xs]))
   pseudo_inverse = dot(inv(dot(xs_t_weighted, xs)), xs_t_weighted)

   weights = dot(pseudo_inverse, ys)
   return dot(transpose(weights), target_x)[0][0]


## testing:
print("For max_deg==3:",
      predict([([0.0], 1.0), ([2.0], 2.0), ([4.0], 3.0), ([6.0], 4.0)],
              [1.2],
              max_deg=3)) ## --> 1.6
print("For max_deg==4:",
      predict([([0.0], 1.0), ([2.0], 2.0), ([4.0], 3.0), ([6.0], 4.0)],
              [1.2],
              max_deg=4)) ## --> not 1.6
