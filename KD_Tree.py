'''.............................
   Creation 2015 by Samuel Tenka
   .............................'''
''' High-dimensional kd-tree'''

import random
def random_coor(num_dimensions):
   return int(random.random()*num_dimensions)
def distance(p1, p2, num_dimensions):
   return sum((p1[i]-p2[i])**2 for i in range(num_dimensions))**0.5

class KD:
   def __init__(self, children, num_dimensions): ## num_dimensions might be < children if, say,
                                                 ## last component is y's and thus not to be
      self.is_leaf = True
      self.children = children
      self.num_dimensions = num_dimensions
      if len(children) > 5:
         self.is_leaf = False
         self.coor = random_coor(self.num_dimensions)
         self.avg = sum(c[self.coor] for c in children)/len(children)
         left = []; right = []
         for c in children:
            (left if c[self.coor]<self.avg else right).append(c)
         self.children = [KD(left, self.num_dimensions),
                          KD(right, self.num_dimensions)]                      
   def neighbors_of(self, point, radius):
      ''' _open_ ball '''
      if self.is_leaf:
         return [c for c in self.children if distance(c, point, self.num_dimensions)<radius]
      else:
         rtrn = []
         if point[self.coor]-radius < self.avg:
            rtrn += self.children[0].neighbors_of(point, radius)
         if point[self.coor]+radius >= self.avg:
            rtrn += self.children[1].neighbors_of(point, radius)
         return rtrn
   def print(self, tabs=0, is_left=None, coor=None, avg=None):
      print('.'+'...'*tabs, '' if is_left==None else
            'x'+str(coor)+('<' if is_left else '>=')+str(avg)+':')
      if self.is_leaf:
         for c in self.children:
            print('.'+'...'*(tabs+1), c)
      else:
         self.children[0].print(tabs+1, is_left=True, coor=self.coor, avg=self.avg)
         self.children[1].print(tabs+1, is_left=False, coor=self.coor, avg=self.avg)


'''
## testing:
c = [(1.0, 1.0), (1.1, 1.1), (1.2, 1.2), (1.3, 1.3), (1.4, 1.4), (2.0, 1.0), (3.0, 1.0), (4.0, 1.0), (5.0, 1.0), (6.0, 1.0), (7.0, 1.0), (8.0, 1.0), (9.0, 1.0), (10.0, 1.0), (11.0, 1.0), (12.0, 1.0)]
K = KD(c)
K.print()
print(K.neighbors_of((1.0, 1.0), 0.5)) ## --> [(1.0, 1.0), (1.1, 1.1), (1.2, 1.2), (1.3, 1.3)]
'''
