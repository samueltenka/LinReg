'''.............................
   Creation 2015 by Samuel Tenka
   .............................'''

import CSV_Reader
import LinearRegression

xys = CSV_Reader.get_xys_from('train_graphs_f16_autopilot_cruise.csv')
predict = LinearRegression.make_predictor(xys, tau=1E9, max_deg=6)
print(predict([0.0058,-2.7,0.0,0,0.014,0.0]))
print(predict([-0.0067,0.1,0.0,10,0.005,0.1]))
print(predict([0.001,-3.9,-0.02,-10,0.019,0.0]))
print(predict([0.0065,3.9,0.0,0,0.017,0.0]))
