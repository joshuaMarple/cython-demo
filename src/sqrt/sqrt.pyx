"""
This module contains a function that returns the square root of a number (float).
"""

def sqrt(float square):
    """    
    Input: square
	square (float): the number to return the square root of.
    Returns:
	A floating point number whose square is the input.
    Description: This function will return the square root of a number.
    """

    cdef float guess
    guess = square / 2
    # if result is negative, raise exception?
    steps = 25
    for __ in xrange(steps):
        guess = (guess + square / guess) / 2
    return guess