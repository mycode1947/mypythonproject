#!/usr/bin/env python
from multiprocessing import Pool
import time
def func1(x):
	print x*x 

if __name__=="__main__":
	for i in range(200):
		func1(i)
