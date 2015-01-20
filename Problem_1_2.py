'''.............................
   Creation 2015 by Samuel Tenka
   .............................'''
''' HW 1.1.2: generates plotpoints for Error v. Reg. Parameter '''

from CSV_Reader import get_xys_from
from LinearRegression import make_predictor
import RMS
from math import exp

train_xys = get_xys_from('train_graphs_f16_autopilot_cruise.csv')
test_xys = get_xys_from('test_graphs_f16_autopilot_cruise.csv')
train_error_of = lambda predictor: RMS.error(train_xys, predictor)
test_error_of = lambda predictor: RMS.error(test_xys, predictor)

predictors = [(L, make_predictor(train_xys, max_deg=6,
                                 reg_param=exp(L))) for L in range(-40, 20+1)]

print("reg_param\ttest rms error\ttrain rms error")
for p in predictors:
   print(p[0], "\t\t", train_error_of(p[1]), \
         "\t", test_error_of(p[1]))
