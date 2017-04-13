#!/usr/bin/env python
line1=raw_input("Please enter a line:")
count=0
for char in line1:
	if count == 0 and char in ['m','i','w','f']:
		char=char.capitalize()
		count+=1
		print char
	else:
		count+=1
		print char
print "end of code"
