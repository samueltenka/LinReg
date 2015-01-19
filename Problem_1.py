'''.............................
   Creation 2015 by Samuel Tenka
   .............................'''

import CSV_Reader
import LinearRegression
import RMS

xys = CSV_Reader.get_xys_from('train_graphs_f16_autopilot_cruise.csv')
predict = LinearRegression.make_predictor(xys, max_deg=6)

print("actual\t  predicted")
print("-10.0\t", predict([0.0058,-2.7,0.0,0,0.014,0.0]))    ## --> ~-10.0
print("-10.0\t", predict([-0.0067,0.1,0.0,10,0.005,0.1]))   ## --> ~-10.0
print("-20.0\t", predict([0.001,-3.9,-0.02,-10,0.019,0.0])) ## --> ~-20.0
print("+20.0\t", predict([0.0065,3.9,0.0,0,0.017,0.0]))     ## --> ~+20.0
print("-20.0\t", predict([0.0021,-2.1,0.0,-40,0.006,-0.1])) ## --> ~-20.0
print("-10.0\t", predict([-0.0117,-1.6,0.0,20,0.012,-0.2])) ## --> ~-10.0
print("-10.0\t", predict([-0.008,-2.0,0.01,-30,0.046,-0.1]))## --> ~-10.0
print("+30.0\t", predict([0.0002,4.9,0.0,0,-0.005,0.2]))    ## --> ~+30.0


null_model = lambda x: 0.0
print("rms error:", RMS.compute_error(xys, predict)) ## --> positive, hopefully small number
print("variance:", RMS.compute_error(xys, null_model)) ## --> positive number, on order of 10
