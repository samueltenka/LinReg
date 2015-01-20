'''.............................
   Creation 2015 by Samuel Tenka
   .............................'''
''' HW 1.4.1: Kaggle Challenge '''

from CSV import get_xys_from, put_xys_to
from KD_Tree import KD
from LinearRegression import make_predictor
from math import sqrt
      
def discretize(pred):
   def rounded(x):
      y = pred(x)
      r = round(y/10.0)*10.0
      if r==0 and y!=0:
         r = 10.0 if y>0 else -10.0
      return r
   return rounded

def statistics(strain):
   avg = sum(strain)/len(strain)
   stddev = sqrt(sum((x-avg)**2 for x in strain))
   return (avg, stddev)
def normalize(x, stats):
   return (x-stats[0])/stats[1]
def unnormalize(strain, stats):
   return (x*stats[1])+stats[0]
   
def make_optimized_predictor(train_xys, max_deg, tau, reg_param):
   xs = [x for (x, y) in train_xys]
   strains = [[x[i] for x in xs] for i in range(len(xs[0]))]
   stats = [statistics(strain) for strain in strains]
   normxs = [[normalize(xi, si) for xi, si in zip(x, stats)] for x in xs]
   put_xys_to('xkcd.csv', [(x, 0) for x in normxs])
   
   K = KD(normxs)

   ## (epsilon ball volume / scattercloud volume) == #points needed / total #points
   ## radius**dim / sqrt(sum of vars)**dim = degs_freedom / len(xs)
   ## radius**dim / sqrt(dim)**dim = dim*(max_deg+1) / len(xs)
   dim = len(xs[0]) ## == 6
   radius = sqrt(dim) * (dim*(max_deg+1)/len(xs))**(1.0/dim)
   def optimized(x):
      neighb_normxs = K.neighbors_of(x, radius)
      print("len", len(neighb_normxs))
      pred = make_predictor(neighb_normxs, max_deg, tau ,reg_param)
      normx = [normalize(xi, si) for xi, si in zip(x, stats)]
      return discretize(pred(normx))
   return optimized

train_xys = get_xys_from('train_graphs_f16_autopilot_cruise.csv')
test_xys = get_xys_from('test_graphs_f16_autopilot_cruise.csv')

xs = [x for (x, y) in train_xys]
p = make_optimized_predictor(train_xys, 6, 1.0, 1.0)
print(p(xs[0]))

