def get_row(file):
   return file.readline().split(',')[1:] ## neglect first val (ID#).
def get_xys_from(filename):
   ''' return format [((x1,...,xn), y),
                      ((x1,...,xn), y),...]'''
   xys = []
   with open(filename) as f:
      f.readline() ## headings, to be discarded
      for row in iter(lambda:get_row(f), []):
         values = [eval(s) for s in row]
         xys.append((values[:-1], values[-1]))
   return xys


## testing:
g = get_xys_from('train_graphs_f16_autopilot_cruise.csv')
print(g[0]) # -->([0.0058, -2.7, 0.0, 0, 0.014, 0.0], -10.0)
print(g[-1]) # --> ([0.0009, 8.7, 0.0, -50, -0.009000000000000001, 0.1], 20.0)
print(len(g)) # --> 3426
