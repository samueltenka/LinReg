'''.............................
   Creation 2015 by Samuel Tenka
   .............................'''
''' Features'''


from math import factorial

#def poly_features(x, max_deg):
#   return [1] + [xi**d/factorial(d) for d in range(1,max_deg+1) for xi in x]
def quad_features(x):
   ''' quad_features([2,3]) --> [1, 2, 4, 3, 6, 9] '''
   x = [1]+x
   return [x[i]*x[j] for i in range(len(x)) for j in range(i+1)]
         

def modify_maker(make_predictor):
   def modified_maker(xys):
      fxys = [(quad_features(x),y) for (x,y) in xys]
      pfxys = make_predictor(fxys)
      def predict(target_x):
         return pfxys(quad_features(target_x))
      return predict
   return modified_maker
