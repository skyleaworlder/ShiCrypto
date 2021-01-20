import random
from ECC import ECC
from PrimeTest import Fermat
from QuadResidue import legendre
from Calcu import Sqrt, GCD, Mul, Inverse
from ConMod import CMVerify

class ECIES:

    def __init__(self, E, P, m, n):
        self.E = E
        self.E.calcuDots()
        assert P in self.E.dots
        self.P = P
        assert GCD(m, n) == 1 and Fermat(n)
        self.m = m
        self.Q = self.E.multi(self.P, self.m)
        self.n = n

    def _point_compress(self, P):
        assert P in self.E.dots
        return (P[0], P[1] % 2)

    def _point_decompress(self, x, i):
        z = self.E._fx(x)
        assert legendre(z, self.E.p) == 1
        '''
        through Sqrt, get 2 solutions, and only need one.
        '''
        y = Sqrt(z, self.E.p)[0]
        return (x, y) if CMVerify(y, i, 2) else (x, self.E.p - y)

    '''
    x is a num in Zp*
    k is a rand num in Zn*
    (y1,y2): y1 is a dot in E, while y2 is a num
    '''
    def encrypt(self, x):
        flag = True
        while flag:
            k = random.randint(2, self.n)
            if GCD(k, self.n) == 1:
                break
        x0y0 = self.E.multi(self.Q, k)
        y1 = self._point_compress(self.E.multi(self.P, k))
        y2 = Mul(x, x0y0[0], self.E.p)
        return (y1, y2)

    '''
    cipher is (y1, y2)
    y1 is a dot in E, while y2 is a num
    '''
    def decrypt(self, cipher):
        print(cipher)
        x0y0 = self.E.multi(
            self._point_decompress(cipher[0][0], cipher[0][1]),
            self.m
        )
        return Mul(
            cipher[1],
            Inverse(x0y0[0], self.E.p),
            self.E.p
        )
