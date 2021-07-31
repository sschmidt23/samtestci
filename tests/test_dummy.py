from code import flux, magnitude, fibonacci
import numpy as np


def fibo_test():
    assert fibonacci(2) == 1

def fluxtest():
    assert np.isclose(flux(-5.),100.)

def magtest():
    assert np.isclose(magnitude(100.), -5.)
