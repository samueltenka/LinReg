'''.............................
   Creation 2015 by Samuel Tenka
   .............................'''
''' High-dimensional kd-tree'''

import random
def random_coor():
   return int(random.random()*2.0)

class KD:
   def __init__(self, children):
      self.is_leaf = True
      self.children = children
      self.coor = self.avg = None
      if len(children) > 5:
         self.is_leaf = False
         self.coor = random_coor()
         self.avg = sum(c[self.coor] for c in children)/len(children)
         left = []; right = []
         for c in children:
            (left if c[self.coor]<self.avg else right).append(c)
         self.children = [KD(left), KD(right)]
   def branch_of(self, point):
      return (self.children[0] if point[self.coor]<self.avg else self.children[1])
   def neighbors_of(self, point):
      return self.children if self.is_leaf else self.branch_of(point).neighbors_of(point)
   def print(self, tabs=0, is_left=None, coor=None, avg=None):
      print('.'+'...'*tabs, '' if is_left==None else
            'x'+str(coor)+('<' if is_left else '>=')+str(avg)+':')
      if self.is_leaf:
         for c in self.children:
            print('.'+'...'*(tabs+1), c)
      else:
         self.children[0].print(tabs+1, is_left=True, coor=self.coor, avg=self.avg)
         self.children[1].print(tabs+1, is_left=False, coor=self.coor, avg=self.avg)


c = [(1.0, 1.0), (1.1, 1.1), (1.2, 1.2), (1.3, 1.3), (1.4, 1.4), (2.0, 1.0), (3.0, 1.0), (4.0, 1.0), (5.0, 1.0), (6.0, 1.0), (7.0, 1.0), (8.0, 1.0), (9.0, 1.0), (10.0, 1.0), (11.0, 1.0), (12.0, 1.0)]
K = KD(c)
K.print()
print(K.neighbors_of((1.0, 1.0)))
