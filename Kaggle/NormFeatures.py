
'''.............................
	Creation 2015 by Samuel Tenka
	.............................'''
''' Normalize'''


from math import sqrt

def statistics(strain):
	avg = sum(strain)/len(strain)
	stddev = sqrt(sum((s-avg)**2 for s in strain)/len(strain))
	return (avg, stddev)

def normalize_coor(xi, ci):
        return (xi-ci[0])/ci[1] if ci[1]!=0 else (xi-ci[0]) ## in case stddev==0
def normalize_point(x, coor_stats):
	return [normalize_coor(xi, ci) for xi,ci in zip(x, coor_stats)]

class Normalizer:
	def __init__(self, xs):
		strains = [[x[i] for x in xs] for i in range(len(xs[0]))]
		self.coor_stats = [statistics(sn) for sn in strains]
		self.norm_xs = [normalize_point(x, self.coor_stats) for x in xs]
	def normalize(self, x):
		return normalize_point(x, self.coor_stats)

def modify_maker(make_predictor):
	def modified_maker(xys):
		N = Normalizer([x for x,y in xys])
		nxys = [(nx,y) for (nx,(x,y)) in zip(N.norm_xs, xys)]
		pnxys = make_predictor(nxys)
		def predict(target_x):
			return pnxys(N.normalize(target_x))
		return predict
	return modified_maker

