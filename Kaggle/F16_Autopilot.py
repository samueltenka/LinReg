import CSV
import LocLinReg
import NormFeatures
import PolyFeatures

from math import sqrt

train1_xys = CSV.get_xys_from('train_graphs_f16_autopilot_cruise.csv')
train2_xys = CSV.get_xys_from('test_graphs_f16_autopilot_cruise.csv')
train_xys = train1_xys + train2_xys[100:]
test_xys = CSV.get_xys_from('test_locreg_f16_autopilot_cruise.csv')
kaggle_xys = CSV.get_xys_from('test_f16_autopilot_cruise.csv',
                              include_ys=False)
def error(pred, xys):
   return sqrt(sum((pred(x)-y)**2 for x,y in xys)/len(xys))
'''
## found tau = 2**(-0.5), lambda = 2**0 works best
for T in range(-5, 5):
   for L in range(-5, 5):
      tau = 2**(T/10.0)
      lam = 2**(L/10.0)
      maker = LocLinReg.make_maker(tau, lam) ## 0.5, 0.25
      maker = NormFeatures.modify_maker(maker)
      maker = PolyFeatures.modify_maker(maker)
      pred = maker(train_xys)
      print(T, L, error(pred, test_xys))
'''
maker = LocLinReg.make_maker(1.31, 1.0)
maker = NormFeatures.modify_maker(maker)
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
