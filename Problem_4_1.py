'''.............................
   Creation 2015 by Samuel Tenka
   .............................'''
''' HW 1.4.1: Kaggle Challenge '''

from CSV_Reader import get_xys_from
from LinearRegression import make_predictor
import RMS
from math import exp

train_xys = get_xys_from('train_graphs_f16_autopilot_cruise.csv')
test_xys = get_xys_from('test_graphs_f16_autopilot_cruise.csv')
train_error_of = lambda predictor: RMS.error(train_xys, predictor)
test_error_of = lambda predictor: RMS.error(test_xys, predictor)

def roundp(pred):
   return lambda x: round(pred(x)/10.0)*10.0
predictor = roundp(make_predictor(train_xys, max_deg=6, reg_param=1.0))
                   
print(test_error_of(predictor))
