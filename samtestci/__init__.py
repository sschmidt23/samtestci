"""unittest module
quick unit test example (to test Travis-CI)
"""
import math
def magnitude(in_flux, zero_point):
    """returns magnitude

    Parameters
    ----------
    flux: 'float'
      float value object flux
    zero_point: 'float'
      float value mag zero point for specific band
    Returns
    -------
    magnitude: 'float'
      object magnitude
    """
    return -2.5*math.log10(in_flux) + zero_point

def flux(mag):
    """returns flux given magnitude

    Parameters
    ----------
    mag: 'float'
      magnitude of object

    Returns
    -------
    flux: 'float'
      object flux
    """
    print("here is a short line")
    return 10.**(-0.4*mag)

def fibonacci(n_n):
    """returns nth number in fibonacci sequence
    Parameters:
    -----------
    n: int
      index of fibonacci desired
    Returns:
    --------
    fib: int
       nth fibonacci number
    """
    x_var,y_var = 0,1
    for _ in range(n_n):
        x_var,y_var = y_var,x_var+y_var
    return x_var
