#inbuilt function 

# user defined function

import math


# pi --> area of cirlce with unit length , r = 1unit
# area = pi * r * r

myvar = 'rupesh'
def cirArea(r):
    area = math.pi * math.pow(r , 2)
    return area

def myGcd(n1,n2):
    g = math.gcd(n1,n2)
    return g


def expnt(a,b):
    p = math.pow(a,b)
    return p


def sqroot(a):
    s = math.sqrt(a)
    return s