#!/usr/bin/env python
def checkevenornot(num):
	if num%2 == 0:
		print "inside the function"
		print "%d is a even number" %(num)
	else:
		print "inside the function"
		print "%d is a odd number" %(num)
if __name__=="__main__":
	num=int(raw_input("Please enter a number:"))
	checkevenornot(num)
