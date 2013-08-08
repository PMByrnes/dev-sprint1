# This is where Exercise 5.4 goes
# Name: Pat Byrnes (PMByrnes)

def is_triangle(a, b, c):
	if (a+b) <= c:
		print 'Not a Triangle'
	elif (a+c) <= b:
		print 'Not a Triangle'
	elif (b+c) <= a:
		print 'Not a Triangle'
	else:
		print 'This is a Triangle'