'''.............................
   Creation 2015 by Samuel Tenka
   .............................'''
''' High-dimensional kd-tree'''

import random
def random_coor():
   return int(random.random()*2.0)
def distance(p1, p2):
   return sum(p1[i]*p2[i] for i in range(len(p1)))**0.5

class KD:
   def __init__(self, children, predicate=lambda x:True, sign=None):
      self.is_leaf = True
      self.children = children
      self.predicate = predicate ## need to and w/all parents' for full strength
      if len(children) > 5:
         self.is_leaf = False
         self.coor = random_coor()
         self.avg = sum(c[self.coor] for c in children)/len(children)
         left = []; right = []
         left_predicate = lambda x: x[self.coor]<self.avg
         right_predicate = lambda x: x[self.coor]>=self.avg
         for c in children:
            (left if left_predicate(c) else right).append(c)
         self.children = [KD(left, left_predicate, -1),
                          KD(right, right_predicate, +1)]
   def intersects(self, point, radius, child_sign):
      return point[self.coor]+radius < self.avg if child_sign==-1 else ## left
             point[self.coor]+radius >= self.avg                       ## right
   def neighbors_of(self, point, radius):
      if self.is_leaf:
         return [c for c in self.children if distance(c, point)<radius]
      else:
         rtrn = []
         if children[0].intersects(point, radius, -1):
            rtrn.append(children[0].neighbors_of(point, radius))
         if children[1].intersects(point, radius, +1):
            rtrn.append(children[1].neighbors_of(point, radius))
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


c = [(1.0, 1.0), (1.1, 1.1), (1.2, 1.2), (1.3, 1.3), (1.4, 1.4), (2.0, 1.0), (3.0, 1.0), (4.0, 1.0), (5.0, 1.0), (6.0, 1.0), (7.0, 1.0), (8.0, 1.0), (9.0, 1.0), (10.0, 1.0), (11.0, 1.0), (12.0, 1.0)]
K = KD(c)
K.print()
print(K.neighbors_of((1.0, 1.0)))
