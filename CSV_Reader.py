'''.............................
   Creation 2015 by Samuel Tenka
   .............................'''
''' CSV reader of files of form:
---HEADING LINE
---DATA LINES of form
------ID,x1,x2,x3,...,xn,y'''

def get_row(file):
   return file.readline().split(',')[1:] ## neglect first val (ID#).
def get_xys_from(filename, include_ys=True):
   ''' return format [((x1,...,xn), y),
                      ((x1,...,xn), y),...]'''
   xys = []
   with open(filename) as f:
      f.readline() ## headings, to be discarded
      for row in iter(lambda:get_row(f), []):
         values = [eval(s) for s in row]
         xy = (values[:-1], values[-1]) if include_ys else \
              (values, None)
         xys.append(xy)
   return xys


'''
## testing:
g = get_xys_from('train_graphs_f16_autopilot_cruise.csv')
print(g[0])  ## --> ([0.0058, -2.7, 0.0, 0, 0.014, 0.0], -10.0)
print(g[-1]) ## --> ([0.0009, 8.7, 0.0, -50, -0.009000000000000001, 0.1], 20.0)
print(len(g))## --> 3426

h = get_xys_from('test_f16_autopilot_cruise.csv', include_ys = False)
print(h[0])  ## --> ([-0.0069, 1.8, 0.0, -70, -0.008, 0.1], None)

'''
