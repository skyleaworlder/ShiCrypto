import sys
from Calcu import Euler
from math import inf

def elemOrder(elem, n):
    order = 1
    while order < n:
        if pow(elem, order, n) == 1:
            return order
        order += 1
    return inf
