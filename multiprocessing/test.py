#!/usr/bin/env python
from multiprocessing import Process
def f1(x):
	return x*x
if __name__=="__main__":
	p=Process(target=f1,args=range(1000))
	p.start()
	p.join()
