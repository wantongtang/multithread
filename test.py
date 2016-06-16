

import time




def fun1(a):
	time.sleep(a)
	print str(a)
	return a



	
from multiprocessing.dummy import Pool as ThreadPool
x=[1,2,3,1,2,1,2,1,2,3,4,1,1,2,2,2,2,2,1,2,2,1,2,1,2] 
pool=ThreadPool(8)
results=pool.map(fun1,x)
pool.close()
pool.join()

for x in range(len(results)):
	print x
