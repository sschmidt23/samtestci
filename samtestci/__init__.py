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
    add a long line to see if pytest complains here ............................................................
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
