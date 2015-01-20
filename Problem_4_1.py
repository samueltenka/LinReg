'''.............................
   Creation 2015 by Samuel Tenka
   .............................'''
''' HW 1.4.1: Kaggle Challenge '''

from CSV import get_xys_from, put_xys_to
from LinearRegression import make_predictor
import RMS
from math import exp

train_xys = get_xys_from('train_graphs_f16_autopilot_cruise.csv')
test_xys = get_xys_from('test_graphs_f16_autopilot_cruise.csv')
test_error_of = lambda predictor: RMS.error(test_xys, predictor)
def roundp(pred):
   return lambda x: round(pred(x)/10.0)*10.0
PREDICTOR = roundp(make_predictor(train_xys, max_deg=6, reg_param=1.0/2.7**2))
print(test_error_of(PREDICTOR))

kaggle_xys = get_xys_from('test_f16_autopilot_cruise.csv',
                          include_ys=False)
completed_xys = [(x, PREDICTOR(x)) for x,y in kaggle_xys]
put_xys_to('abc.csv', completed_xys, include_xs=False)
