'''.............................
   Creation 2015 by Samuel Tenka
   .............................'''
''' HW 1.4.1: Kaggle Challenge '''

from CSV import get_xys_from, put_xys_to
from KD_Tree import KD
from LinearRegression import make_predictor
from DataNormalizer import Normalizer
      
def discretize(pred):
   def rounded(x):
      y = pred(x)
      r = round(y/10.0)*10.0
      if r==0 and y!=0:
         r = 10.0 if y>0 else -10.0
      return r
   return rounded
   
def make_optimized_predictor(train_xys, max_deg, tau, reg_param):
   xs = [x for (x, y) in train_xys]
   N = Normalizer(xs)
   norm_xs = N.norm_xs
   norm_xys = [nx+[y] for (nx,(x,y)) in zip(norm_xs, train_xys)]
   
   K = KD(norm_xys, len(xs[0])) ## so don't allow partitioning by y

   ## (epsilon ball volume / scattercloud volume) == #points needed / total #points
   ## radius**dim / sqrt(sum of vars)**dim = degs_freedom / len(xs)
   ## radius**dim / sqrt(dim)**dim = dim*(max_deg+1) / len(xs)
   dim = len(xs[0]) ## == 6
   radius = (dim**0.5) * (dim*(max_deg+1)/len(xs))**(1.0/dim)
   #print('radius', radius)
   def optimized(x):
      norm_x = N.normalize(x)
      nbd_norm_xys = K.neighbors_of(norm_x, radius)
      xys = [(xy[:-1], xy[-1]) for xy in nbd_norm_xys]
      #print("len", len(xys))
      pred = make_predictor(xys, max_deg, tau, reg_param)
      return discretize(pred)(norm_x)
   return optimized

train_xys = get_xys_from('train_graphs_f16_autopilot_cruise.csv')
test_xys = get_xys_from('test_graphs_f16_autopilot_cruise.csv')

xs = [x for (x, y) in train_xys]
p = make_optimized_predictor(train_xys, 6, 1.0, 1.0)
print(p(xs[0]))

