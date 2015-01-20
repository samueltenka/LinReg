'''.............................
   Creation 2015 by Samuel Tenka
   .............................'''

from CSV_Reader import get_xys_from
from LinearRegression import make_predictor
import RMS
from math import exp
from random import random

train_xys = get_xys_from('train_graphs_f16_autopilot_cruise.csv')
test_xys = get_xys_from('test_graphs_f16_autopilot_cruise.csv')
train_error_of = lambda predictor: RMS.error(train_xys, predictor)
test_error_of = lambda predictor: RMS.error(test_xys, predictor)
null_model = lambda x: 0.0

def generate_predictors(max_deg):
   for log_lambda in range(-40, 20+1):
      print((max_deg, log_lambda), end="  ")
      pred = make_predictor(train_xys, max_deg=max_deg,
                            reg_param=exp(log_lambda))
      yield pred
def get_predictor(max_deg):
   rtrn = min((train_error_of(pred), random(), pred)
              for pred in generate_predictors(max_deg))
   #rtrn = (error_of(null_model), null_model)
   #for pred in generate_predictors(max_deg):
   #   error = train_error_of(pred)
   #   if error < rtrn[0]:
   #      rtrn = (error, pred)
   print("\n", rtrn[0], "\n\n")
   return rtrn[2]

predictors = [null_model] + [get_predictor(i) for i in range(1, 6+1)]

print("null model's error:", test_error_of(null_model))
print()
print("maximum\t\trms error")
print(" degree             ")
for i in range(1, 6+1):
   print(i, "\t\t", test_error_of(predictors[i]))


'''
maximum		rms error
 degree             
1 		 14.8112273159
2 		 14.8342486623
3 		 14.7246665024
4 		 14.8121911411
5 		 14.8784538269
6 		 14.9338347157
'''
