'''.............................
   Creation 2015 by Samuel Tenka
   .............................'''
''' HW 1.1.1: generates plotpoints of Error v. Polynomial Degree'''

from CSV_Reader import get_xys_from
from LinearRegression import make_predictor
import RMS
from math import exp

train_xys = get_xys_from('train_graphs_f16_autopilot_cruise.csv')
test_xys = get_xys_from('test_graphs_f16_autopilot_cruise.csv')
test_error_of = lambda predictor: RMS.error(test_xys, predictor)
null_model = lambda x: 0.0

predictors = [null_model] + [make_predictor(train_xys, max_deg=i) for i in range(1, 6+1)]

print("null model's error:", test_error_of(null_model))
print()
print("maximum\t\trms error")
print(" degree             ")
for i in range(1, 6+1):
   print(i, "\t\t", test_error_of(predictors[i]))
