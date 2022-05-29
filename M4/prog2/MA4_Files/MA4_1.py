import numpy as np
import matplotlib.pyplot as plt
import math
import functools
from time import perf_counter as pc
from time import sleep
import multiprocessing as mp
import concurrent.futures as future

# 1.1

def monte_pi(n):
	x = np.random.uniform(-1,1,n)
	y = np.random.uniform(-1,1,n)

	#plt.plot(x,y,'s')
	#plt.show()

	outside = 0
	inside = 0

	p_inx = []
	p_outx = []
	p_iny = []
	p_outy = []

	for i in range(0,n):
		length = math.sqrt(x[i]**2 + y[i]**2)
		if length >= 1:
			outside += 1
			p_outx.append(x[i])
			p_outy.append(y[i])
		elif length < 1:
			inside += 1
			p_inx.append(x[i])
			p_iny.append(y[i])

	print("Inside: " + str(inside))
	print("Outside: " + str(outside))

	pi_app = 4*inside/n

	print("PI approximation: " + str(pi_app))
	print("PI: " + str(math.pi))

	plt.plot(p_inx,p_iny,'ro')
	plt.plot(p_outx,p_outy,'bo')
	plt.savefig("monte_pi.png")
	plt.show()

# 1.2

def monte_multi(n,d):

	#n = 1000000
	#d = 11
	inside = 0

	f = lambda x : x**2

	for i in range(n):
		point = [np.random.uniform(-1,1,) for j in range(d)]
		length = functools.reduce(lambda x,y : x+y, list(map(f,point)))

		if length <= 1:
			inside += 1

	volume = 2**d * (inside / n)
	volume_true = (math.pi**(d/2))/math.gamma(d/2 + 1)

	print("Approximation of volume: " + str(volume))
	print("True volume: " + str(volume_true))

# 1.3

def parallel():
	# Non-parallel
	#start = pc()
	#monte_multi(10000000,11)
	#end = pc()
	#print(f"Process took {round(end-start,2)} seconds")
	# Process took 451.72 seconds

	# write for loop that makes average

	# parallel
	start = pc()
	with future.ProcessPoolExecutor() as ex:
		n = [1000000] * 10
		d = [11] * 10
		results = ex.map(monte_multi,n,d)
	end = pc()
	#Process took 41.58 seconds

	print(f"Process took {round(end-start,2)} seconds")

def main():

	# Redovisning 1.1
	#nn = [1000,10000,100000]
	#for n in nn:
	#	monte_pi(n)

	# Redovisning 1.2
	#monte_multi(100000,2)
	#monte_multi(100000,11)

	# Redovisning 1.3
	parallel()

	

if __name__ == '__main__':
	main()