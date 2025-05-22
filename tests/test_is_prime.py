import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from examples.example_error_handling import is_prime

def test_is_prime_basic():
    assert is_prime(2)
    assert is_prime(3)
    assert not is_prime(4)
    assert is_prime(13)
    assert not is_prime(1)
