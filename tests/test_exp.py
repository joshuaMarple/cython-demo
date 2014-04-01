import sys, os
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/Exponential'))
if not path in sys.path:
    sys.path.insert(1, path)
import Exponential
del path

def test_Exp():
    assert Exponential.Exp(4,2) == 16

def test_b():
    assert 'b' == 'b'
