"""
This module contains a function that allows you to do a factorial of a positive integer.
"""

def factorial(int n):
	"""
	Input: n
	n (integer): the number to do the factorial function on
	Returns: The value of n!
	Description: This function will return n!
	"""
	
	if n < 0:
		return "n must be positive to do n!"
	elif n == 0:
		return 1
	else:
		return n * factorial(n - 1)
