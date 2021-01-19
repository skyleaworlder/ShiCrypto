import sys
from Calcu import Euler, GCD
from ConMod import DIVVerify, CMVerify
from math import ceil, sqrt
from sympy import prime

'''
Trial
'''
def elemOrder(elem, n):
    order = 1
    while order < n:
        if pow(elem, order, n) == 1:
            return order
        order += 1
    return float('inf')

'''
use phi to verify
whether g is primit root or not
'''
def primVerify(g, m):
    order = elemOrder(g, m)
    if order == Euler(m):
        return True
    else:
        return False

'''
use theory about:
m > 2, phi(m)'s prime factor q_i, gcd(g, m) = 1, st.
g^{\\frac{phi(m)}{q_i}} != 1 (mod m) <==> g is a primitive root.
'''
def primVerify2(g, m):
    assert GCD(g, m) == 1

    phi = Euler(m)
    prime_fac = []

    index = 1
    prim = prime(index)
    bound = ceil(sqrt(phi))
    while prim < bound:
        if DIVVerify(prim, phi):
            prime_fac.append(prim)
        index += 1
        prim = prime(index)

    for q in prime_fac:
        if CMVerify(pow(g, phi // q), 1, m):
            return False
    else:
        return True

'''
return the order of elem^lamb
'''
def elemPowOrder(elem, lamb, n):
    order = elemOrder(elem, n)
    return order // GCD(lamb, order)
