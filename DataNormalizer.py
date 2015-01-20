def statistics(strain):
   avg = sum(strain)/len(strain)
   stddev = (sum((x-avg)**2 for x in strain)/len(strain))**0.5
   return (avg, stddev)

def normalize_point(x, coor_stats):
   return [(x[i]-coor_stats[i][0])/coor_stats[i][1] for i in range(len(x))]
def unnormalize_point(x, coor_stats):
   return [(x[i]*coor_stats[i][1])+coor_stats[i][0] for i in range(len(x))]

class Normalizer:
   def __init__(self, xs):
      self.coor_strains = [[x[i] for x in xs] for i in range(len(xs[0]))]
      self.coor_stats = [statistics(sn) for sn in self.coor_strains]
      #print(self.coor_stats)
      self.norm_xs = [normalize_point(x, self.coor_stats) for x in xs]
   def normalize(self, x):
      return normalize_point(x, self.coor_stats)
   def unnormalize(self, x):
      return unnormalize_point(x, self.coor_stats)
