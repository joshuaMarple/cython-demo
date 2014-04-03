import sys, os
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/sqrt'))
if not path in sys.path:
    sys.path.insert(1, path)
import sqrt
del path

def test_sqrt():
    assert sqrt.sqrt(256) == 16
