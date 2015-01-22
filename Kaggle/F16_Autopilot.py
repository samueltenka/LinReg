import CSV
import LocLinReg
import NormFeatures
import PolyFeatures

from math import sqrt

train1_xys = CSV.get_xys_from('train_graphs_f16_autopilot_cruise.csv')
train2_xys = CSV.get_xys_from('test_graphs_f16_autopilot_cruise.csv')
train_xys = train1_xys + train2_xys
test_xys = CSV.get_xys_from('test_locreg_f16_autopilot_cruise.csv')
kaggle_xys = CSV.get_xys_from('test_f16_autopilot_cruise.csv',
                              include_ys=False)

def error(pred, xys):
   return sqrt(sum((pred(x)-y)**2 for x,y in xys)/len(xys))

'''
## find best hyperparameters ## IDEA ABOUT TERRACED LEVELS OF HYPERNESS/DATA DIVISION
def error_of(tau, reg_param):
   maker = LocLinReg.make_maker(tau, reg_param)
   maker = NormFeatures.modify_maker(maker)
   maker = PolyFeatures.modify_maker(maker)
   pred = maker(train_xys)
   return error(pred, test_xys)

for T in range(-7, 0):
   for L in range(-7, 0):
      tau = 2**T
      lam = 2**L
      print(tau, '\t', lam, '\t', error_of(tau, lam))
'''

## testing:
maker = LocLinReg.make_maker(0.25, 0.125)
maker = PolyFeatures.modify_maker(maker)
pred = maker(train_xys)

print(error(pred, test_xys))
xys = []
i = 0
for (x,y) in kaggle_xys:
   if i%100==0:
      print(i)
   i += 1
   xys.append((x, pred(x)))
      
CSV.put_xys_to('smbc.csv', xys, include_xs=False)

'''
print(pred([ 0.0058, -2.7,  0   ,  0, 0.014, 0  ])) ## --> ~-10
print(pred([-0.0067,  0.1,  0   , 10, 0.005, 0.1])) ## --> ~-10
print(pred([ 0.001 , -3.9, -0.02,-10, 0.019, 0  ])) ## --> ~-20
print(pred([ 0.0065,  3.9,  0   ,  0, 0.017, 0  ])) ## --> ~+20
print(pred([ 0.0021, -2.1,  0   ,-40, 0.006,-0.1])) ## --> ~-20
'''
