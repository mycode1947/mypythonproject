#!/usr/bin/env python
def generatefib(num):
	a=[0,1]
        num=num-1
	for i in range(num):
		a.append(a[-1]+a[-2]) 	
	print a
	return a


print "Please enter the nth fibonacci number"
num=int(raw_input("::"))	
value=generatefib(num)
print value
print value[-1]
