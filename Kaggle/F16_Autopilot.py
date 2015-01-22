import CSV
import LocLinReg
import NormFeatures
import PolyFeatures

from math import sqrt

train_xys = CSV.get_xys_from('train_graphs_f16_autopilot_cruise.csv')
test_xys = xys = CSV.get_xys_from('test_locreg_f16_autopilot_cruise.csv')
def error(pred, xys):
   return sqrt(sum((pred(x)-y)**2 for x,y in xys)/len(xys))

def error_of(tau, reg_param):
   maker = LocLinReg.make_maker(tau, reg_param)
   #maker = NormFeatures.modify_maker(maker)
   maker = PolyFeatures.modify_maker(maker)
   pred = maker(train_xys)
   return error(pred, test_xys)

for T in range(-5, 5):
   for L in range(-5, 5):
      tau = 2**T
      lam = 2**L
      print(tau, '\t', lam, '\t', error_of(tau, lam))


'''
print(predictor([ 0.0058, -2.7,  0   ,  0, 0.014, 0  ])) ## --> ~-10
print(predictor([-0.0067,  0.1,  0   , 10, 0.005, 0.1])) ## --> ~-10
print(predictor([ 0.001 , -3.9, -0.02,-10, 0.019, 0  ])) ## --> ~-20
print(predictor([ 0.0065,  3.9,  0   ,  0, 0.017, 0  ])) ## --> ~+20
print(predictor([ 0.0021, -2.1,  0   ,-40, 0.006,-0.1])) ## --> ~-20
'''
