'''.............................
   Creation 2015 by Samuel Tenka
   .............................'''
''' Features'''


from math import factorial

def factor(*args):
   return 1.0/factorial(sum(1 for x in args if x!=0))
def linr_features(x):
   ''' linr_features([2,3]) --> [1, 2, 3] '''
   return [1]+x
def quad_features(x):
   ''' quad_features([2,3]) --> [1, 2, 4/2, 3, 6/2, 9/2] '''
   x = [1]+x
   return [x[i]*x[j]*factor(i, j) for i in range(len(x)) for j in range(i+1)]
def cubi_features(x):
   ''' cubi_features([2,3]) --> [1, 2, 4/2, 8/6, 3, 6/2, 12/6, 9/2, 18/6, 27/6] '''
   x = [1]+x
   return [x[i]*x[j]*x[k]*factor(i, j, k) for i in range(len(x))
                                          for j in range(i+1)
                                          for k in range(j+1)]
features = quad_features

def modify_maker(make_predictor):
   def modified_maker(xys):
      fxys = [(features(x),y) for (x,y) in xys]
      pfxys = make_predictor(fxys)
      def predict(target_x):
         return pfxys(features(target_x))
      return predict
   return modified_maker
