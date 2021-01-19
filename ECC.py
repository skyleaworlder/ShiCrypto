'''
1. python ECC.py [<a>] [<b>] [<p>] -d
eg. python ECC.py 1 6 11 -d

2. python ECC.py [<a>] [<b>] [<p>] -a/--add [<point-str>] [<point-str>]
need input str command param
eg. python ECC.py 1 6 11 -a "(2,7)" "(2,7)"

3. python ECC.py [<a>] [<b>] [<p>] -m/--mul/--multi [<point-str>] [<times>] [<choice>]
need input str command param
eg. python ECC.py 1 6 11 -m "(2,7)" 7
    python ECC.py 1 6 11 -m "(2,7)" 1100 --naf
'''
import sys
import numpy as np
from PrimeTest import Fermat
from Calcu import Inverse, Add, Sub, Mul, Div, Sqrt
from QuadResidue import legendre
from math import ceil, inf, log2

class ECC:

    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        assert Fermat(p)
        self.p = p
        self.dots = [(inf, inf)]

    def _fx(self, x):
        return x**3 + self.a*x + self.b

    def _check_exist(self, P):
        return (self._fx(P[0]) % self.p == Mul(P[1], P[1], self.p)) or (P == (inf, inf))

    def _NAF(self, num):
        num_bit = []
        ''' ceil+2 because when num equal 2^i '''
        for i in range(1, ceil(log2(num))+2):
            num_bit.append(1) if num % (2**i) - num % (2**(i-1)) != 0 else num_bit.append(0)
        num_bit.append(0)
        L = np.array(num_bit)
        index = [0, 0]
        while index[0] < L.shape[0]-1 and index[1] < L.shape[0]-1:
            '''
            if local elem is 0, or local elem is 1 but next is 0
            index auto increment continually
            '''
            if L[index[0]] == 0 or L[index[0]+1] == 0:
                index[0], index[1] = index[0]+1, index[1]+1
            else:
                '''
                keep index[0] and make index[1] move forward
                when index[1] meets 0 but 1, index[1] stop
                '''
                L[index[0]] = -1
                index[1] += 1
                while index[1] < L.__len__() and L[index[1]] != 0:
                    L[index[1]] = 0
                    index[1] += 1
                L[index[1]] = 1
                index[0] = index[1]
        ''' keep msb 1 '''
        print(L)
        L = L[:-1] if L[L.shape[0]-1] == 0 else L
        return L

    def calcuDots(self):
        '''
        y^2 = z = x^3 + a*x^ + b
        '''
        X = range(0, self.p)
        Z = [self._fx(x) % self.p for x in X]
        Y = []
        for z in Z:
            Y.append(tuple(Sqrt(z, self.p))) if legendre(z, self.p) == 1 else Y.append((-1, -1))

        self.dots = []
        for x, y in zip(X, Y):
            if y != (-1, -1):
                self.dots.append((x, y[0]))
                self.dots.append((x, y[1]))
        self.dots.append((inf, inf))

    def add(self, P, Q):
        assert (self._check_exist(P) and self._check_exist(Q))
        '''
        0. P=O|Q=O: RET P or Q
        1. P+Q=O:   RET (inf, inf)
        2. P=Q:     lambda = dy/dx = (3x_1^2 + a)/2y_1
        3. ELSE:    lambda = delta y / delta x
        '''
        if P == (inf, inf) or Q == (inf, inf):
            return P if Q == (inf, inf) else Q
        elif P[0] == Q[0] and Add(P[1], Q[1], self.p) == 0:
            return (inf, inf)
        elif P == Q:
            lamb = Div(
                Add(3*P[0]**2, self.a, self.p),
                Mul(2, P[1], self.p), (self.p)
            )
        else:
            lamb = Div(
                Sub(Q[1], P[1], self.p),
                Sub(Q[0], P[0], self.p), (self.p)
            )
        '''
        sum_{i=1}^3 x_i = lambda^2
        y_3 = lambda(x_3 - x_1)
        '''
        Rx = (lamb**2 - P[0] - Q[0]) % self.p
        Ry = (lamb*(Q[0] - Rx) - Q[1]) % self.p
        return (Rx, Ry)

    def nega(self, P):
        return (P[0], self.p - P[1])

    '''
    square-multi alg
    such as 1100000, using 6.2s
    '''
    def multi(self, P, k):
        assert k != 0
        if k == 1:
            return P
        elif k % 2 == 0:
            return self.add(self.multi(P, k//2), self.multi(P, k//2))
        else:
            return self.add(P, self.multi(P, k-1))

    '''
    using NAF and square-multi ALG
    in order to decrease time complexity
    such as 1100000, using 1.97s
    '''
    def multi_NAF(self, P, k):
        assert k != 0
        k_bitset = self._NAF(k)
        res = self.multi(P, pow(2, k_bitset.__len__()-1))
        for index,bit in enumerate(k_bitset[:-1]):
            minu_add = self.multi(P, pow(2, index))
            if bit == -1:
                res = self.add(res, self.nega(minu_add))
            elif bit == 1:
                res = self.add(res, minu_add)
            else:
                pass
            print(res)
        return res

def main(argv):
    a,b,p = map(int, (argv[0],argv[1],argv[2]))
    ecc = ECC(a, b, p)

    if argv[3] == "-d" or argv[3] == "--dots":
        ecc.calcuDots()
        print(ecc.dots.__len__(), "dots are:", "( y^2 = x^3 +", ecc.a, "* x +", ecc.b,")")
        for index,dot in enumerate(ecc.dots):
            print(index, ":", dot)
    elif argv[3] == "-a" or argv[3] == "--add":
        P, Q = tuple(eval(argv[4])), tuple(eval(argv[5]))
        print(P, "+", Q, "=", ecc.add(P, Q))
    elif argv[3] == "-m" or argv[3] == "--mul" or argv[3] == "--multi":
        P = tuple(eval(argv[4]))
        k = int(argv[5])
        if argv.__len__() == 7 and argv[6] == "--naf":
            print(P, "*", k, "=", ecc.multi_NAF(P, k), "using NAF")
        else:
            print(P, "*", k, "=", ecc.multi(P, k))
    else:
        pass

if __name__ == "__main__":
    main(sys.argv[1:])
