'''.............................
   Creation 2015 by Samuel Tenka
   .............................'''
''' Linear Regression Error Calculator'''

def compute_error(xys, predictor):
   sum_squares = sum((predictor(x)-y)**2 for (x, y) in xys)
   RMS = (sum_squares/len(xys))**0.5
   return 0.0 if RMS < 1E-12 else RMS ## rounding


## testing:
import LinearRegression
xys = [([0.0], 1.0), ([2.0], 2.0), ([4.0], 3.0), ([6.0], 4.0)]
predictor = LinearRegression.make_predictor(xys, max_deg=3)
print(compute_error(xys, predictor)) ## --> 0.0

xys = [([0.0], 0.0), ([2.0], 4.0), ([4.0], 16.0), ([6.0], 36.0)]
predictor = LinearRegression.make_predictor(xys, max_deg=1)
print(compute_error(xys, predictor)) ## --> strictly > 0.0

