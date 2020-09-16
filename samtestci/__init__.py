"""unittest module
quick unit test example (to test Travis-CI)
"""
import math
def magnitude(flux, zeroPoint):
    """returns magnitude 

    Parameters
    ----------
    flux: 'float'
      float value object flux
    zeroPoint: 'float'
      float value mag zero point for specific band
    Returns
    -------
    magnitude: 'float'
      object magnitude
    """
    return -2.5*math.log10(flux) + zeroPoint

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
    print("here is a very long line to test whether the linter will complain or not, this should make the linter score a little lower than 10/10")
    return 10.**(-0.4*mag)

def fibonacci(n):
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
    x,y = 0,1
    for _ in range(n):
        x,y = y,x+y
    return x 
