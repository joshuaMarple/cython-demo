import sys, os
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../src'))
if not path in sys.path:
    sys.path.insert(1, path)
import primes
del path

def test_primes():
    assert primes.primes(1) == [2]

def test_b():
    assert 'b' == 'b'
