import sys, os
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/Factorial'))
if not path in sys.path:
    sys.path.insert(1, path)
import factorial
del path

def test_factorial():
	assert factorial.factorial(0) == 1
	assert factorial.factorial(1) == 1
	assert factorial.factorial(-1) == "n must be positive to do n!"

def test_n():
	assert 'n' == 'n'
