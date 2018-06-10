import math
def magnitude(flux,zeropt):
    return -2.5*math.log10(flux) + zeropt

def flux(mag):
    return 10.**(-0.4*mag)
