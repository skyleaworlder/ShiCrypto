from QuadResidue import legendre
from PrimeTest import Fermat
from ConMod import CMVerify, DIVVerify, DIVNum
from Calcu import GCD
from math import sqrt, ceil
from functools import reduce
from continued import continuedFrac

'''
Pollard-Rho ALG to decompose a composite number.
n:      the num to decomped
mode:   1. --origin, use f(x) = x^2 - 1 (mod n)
        2. --nowadays, use f(x) = x^2 - 1 (mod n) (default)
        (the second one is recommended)
        (the firset cannot work well in some situations)
'''
class PollardRho:

    def __init__(self, n):
        self.n = n

    def _fx_origin(self, x):
        return (x*x - 1) % self.n

    def _fx_nowadays(self, x):
        return (x*x + 1) % self.n

    '''
    x_0 = 1
    y_0 = f(x_0)
    d = gcd(x, y)

    x <- f(x)
    y <- f(f(y))
    d <- gcd(|x-y|, n)
    '''
    def factoring(self, mode):
        x = 1
        y = self._fx_origin(x) if mode == "--origin" else self._fx_nowadays(x)
        d = GCD(x, y)

        while d == 1:
            x = self._fx_origin(x) if mode == "--origin" else self._fx_nowadays(x)
            y = self._fx_origin(self._fx_origin(y)) if mode == "--origin" else self._fx_nowadays(self._fx_nowadays(y))
            d = GCD(abs(x-y), self.n)

        if d == self.n:
            return -1
        else:
            return d

'''
Fermat Integer-Factorization ALG
if n can have factors p, q
    and a = (p+q)/2, b = (p-q)/2
    then a^2 - b^2 = n
    try to find a^2(a square larger than n)
n:          input for decomped
iterNum:    iter times
'''
def FermatFactor(n, iterNum=512):
    factors = []
    if DIVVerify(2, n):
        n = n // pow(2, DIVNum(2, n))
        factors.append(2)

    def _isSquare(n):
        return pow(int(ceil(sqrt(n))), 2) == n

    beg = int(ceil(sqrt(n)))
    for i in range(iterNum):
        x = beg + i
        if _isSquare(pow(x, 2) - n) \
            and x + sqrt(pow(x, 2) - n) != 1 \
            and x - sqrt(pow(x, 2) - n) != 1:
            factors.append(x + sqrt(pow(x, 2) - n))
            factors.append(x - sqrt(pow(x, 2) - n))
            return factors
    return factors

'''
Wiener Attack
    by calcuing the continued fractions of n/b
    (n/b, instead of b/n on the slides)
n:      input number to decomped
b:      public key
(WARNING: n must be larger than b)
'''
def WienerAttack(n, b):

    ''' solve simple equation: ax^2 + bx + c = 0 '''
    def _solve(a, b, c):
        delta = pow(b, 2) - 4*a*c
        return (-b + sqrt(delta))/(2*a), (-b - sqrt(delta))/(2*a)

    assert n > b
    a = [n//b]
    p = [a[0]]
    q = [1]
    nume_tmp, deno_tmp = b, n-(n//b)*b

    while p[-1] != n and q[-1] != b:
        '''
        Solution Generate Block
        this Block is in front of next Block, cos:
            when len(a), len(p), len(q) = 1
            still need test
        eg. n=90581, b=17993,
            when p=5, q=1,
            n can be factorized
        '''
        ''' check Wiener win or not, and calculate '''
        if DIVVerify(q[-1], p[-1]*b - 1):
            phi = (p[-1]*b - 1) // q[-1]
            ''' delta < 0, none solution '''
            if pow(n-phi+1, 2) - 4*n < 0:
                continue
            x_1, x_2 = _solve(1, -(n-phi+1), n)
            print(x_1, x_2)
            if x_1 * x_2 == n:
                return (x_1, x_2)

        '''
        Continued Fractions Generation Block
        append new elem in a, p, q
        refresh a[-1], p[-1], q[-1]
        '''
        ''' append elem in a '''
        a.append(nume_tmp // deno_tmp)
        nume_tmp, deno_tmp = deno_tmp, nume_tmp-(nume_tmp // deno_tmp) * deno_tmp

        ''' generate convergent p/q '''
        if len(a) == 2:
            ''' first time '''
            p.append(a[0]*a[1]+1)
            q.append(a[1])
        else:
            ''' second to last '''
            k = len(a) - 1
            p.append(a[k]*p[k-1]+p[k-2])
            q.append(a[k]*q[k-1]+q[k-2])

    ''' Wiener Attack Failed '''
    return (-1, -1)
