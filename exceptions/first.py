#!/usr/bin/env python
if __name__=="__main__":
	a=raw_input("Please enter the value for a:")
	b=raw_input("Please enter the value for b:")
	try:
		b=int(b)
		a=int(a)
		value=a/b
		print "division of b by a is %d" %(value)
	except ZeroDivisionError:
		print "Division by 0 is not possible"
	except TypeError:
		print "Division by string is not possible"
	except ValueError:
		print "don't give strings to integer values"
