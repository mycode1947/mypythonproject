#!/usr/bin/env python
from multiprocessing import Pool
import time
def func1(x):
	return x*x 

if __name__=="__main__":
	p=Pool(processes=5)
	print (p.map(func1, range(200), chunksize=10))
