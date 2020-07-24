'''
1. Quadratic Sieve
python IntFactorize.py --QuadSieve/-qs [<number>] [<base-num>]
eg. python IntFactorize.py --QuadSieve 110 100
    python IntFactorize.py -qs 11004 100

2. Pollard Rho
python IntFactorize.py --Rho/-r [<mode>] [<number>]
eg. python IntFactorize.py --Rho --origin 110
    python IntFactorize.py -r --nowadays 110

3. Fermat Factorization
python IntFactorize.py --Fermat/-f [<number>] [<iterNum>]
eg. python IntFactorize.py -f 11011 100
    python IntFactorize.py --Fermat 11 100

4. Wiener Attack
python IntFactorize.py --Wiener/-w [<number>] [<public-key-b>]
eg. python IntFactorize.py -w 160523347 60728973
    python IntFactorize.py --Wiener 160523347 60728981
'''
import sys
from QuadResidue import legendre
from PrimeTest import Fermat
from ConMod import CMVerify, DIVVerify, DIVNum
from Calcu import GCD
from math import sqrt, ceil
import numpy as np
from functools import reduce
from continued import continuedFrac

'''
draft of quadratic sieve.
cannot work and perform well for several reasons.
'''
solve = []
class QuadSieve:

    def __init__(self, n):
        self.n = n
        self.p = []
        self.q = []

    def _Y_calcu(self, x, n):
        return (x + ceil(sqrt(n)))**2 - n

    def _DIV_total(self, base, v):
        ret = v
        cnt = 0
        while DIVVerify(base, ret):
            ret = ret // base
            cnt += 1
        return {
            "ret": ret,
            "cnt": cnt
        }

    def _solve_backTrack(self, coef, ans, layer):
        '''
        back track method
        to find a vector can solve cong_equ
        '''
        global solve
        if layer == ans.shape[1]:
            return
        for i in range(1, -1, -1):
            ans[0][layer] = i
            if (np.mod(np.dot(ans, coef), 2) == np.zeros([ans.shape[0], coef.shape[1]], dtype=int)).all() \
                and (np.array(ans, dtype=int) != np.zeros(ans.shape, dtype=int)).any():
                solve.append(ans[0].tolist())
                #print(ans[0].tolist(), solve)
            #print(layer, "?", ans)
            self._solve_backTrack(coef, ans, layer+1)

    def _solve(self, coef):
        ans = np.zeros([1, coef.shape[0]], dtype=int)
        self._solve_backTrack(coef, ans, layer=0)
        return solve

    def QuadSieve(self, baseNum):
        '''
        V:      vector of Y(x)
        B:      prime bases arr
        Coef:   a matrix(B.len*B.len) of decomped result,
                the same as Coef Matrix in Dixon ALG
        Y:      res
        '''
        global solve
        assert not Fermat(self.n)
        self.V = [self._Y_calcu(x, self.n) for x in range(0, 100)]
        V_tmp = self.V
        self.B = [x for x in range(2, baseNum) if legendre(self.n, x) == 1 and Fermat(x)]

        for base in self.B:
            V_tmp = [self._DIV_total(base, v)["ret"] for v in V_tmp]

        Y_index_arr = [index for index, v in enumerate(V_tmp) if v == 1]
        self.Y = [self.V[index] for index in Y_index_arr]

        ''' div y by base^k if base^k | y '''
        self.Coef = np.zeros([self.Y.__len__(), self.B.__len__()], dtype=int)
        for jndex,y in enumerate(self.Y):
            for index,base in enumerate(self.B):
                self.Coef[jndex][index] = self._DIV_total(base, y)["cnt"]
        self.Coef = np.mod(self.Coef, 2)

        ''' del all 0 rows '''
        res_row = [index for index,val in enumerate(self.Coef.any(axis=1)) if val]
        Y_index_arr = [val for index,val in enumerate(Y_index_arr) if index in res_row]
        self.Coef = self.Coef[res_row, :]

        ''' solve cong_equ(mod 2) '''
        self.R = self._solve(self.Coef)
        #print(self.V, '\n', V_tmp, self.R, solve, Y_index_arr, "???")

        ''' resolve and calcu p_arr, q_arr '''
        for r in self.R:
            Y_index_arr_turn = [val for index,val in enumerate(Y_index_arr) if r[index] != 0]
            square = reduce(lambda x,y : x*self.V[y], Y_index_arr_turn, 1)
            V_2 = [self._Y_calcu(x, self.n)+self.n for x in Y_index_arr_turn]
            square2 = reduce(lambda x,y : x*y, V_2, 1)
            self.p.append(GCD(sqrt(square) + sqrt(square2), self.n))
            self.q.append(GCD(abs(sqrt(square2) - sqrt(square)), self.n))
        print(self.p, '\n', self.q)

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
        return pow(ceil(sqrt(n)), 2) == n

    beg = ceil(sqrt(n))
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

def main(argv):
    choice = argv[0]
    if choice == "--QuadSieve" or choice == "-qs":
        n = int(argv[1])
        baseNum = int(argv[2])
        qs = QuadSieve(n)
        qs.QuadSieve(baseNum)
    elif choice == "--Rho" or choice == "-r":
        mode = argv[1]
        n = int(argv[2])
        rho = PollardRho(n)
        ans = rho.factoring(mode)
        if ans == -1:
            print("Failure.", n, "might be a prime.")
        else:
            print("Success:", n, "can be decomped to", ans, "and", n // ans)
    elif choice == "--Fermat" or choice == "-f":
        n = int(argv[1])
        iterNum = int(argv[2])
        ans = FermatFactor(n, iterNum)
        if ans == []:
            print("Failure.", n, "might be a prime, or try larger iterNum again.")
        else:
            print("Success.", ans, "are factors of", n)
    elif choice == "--Wiener" or choice == "-w":
        n = int(argv[1])
        b = int(argv[2])
        ans = WienerAttack(n, b)
        if ans == (-1, -1):
            print("Failure.", n, "cannot be factorized by this methods")
        else:
            print("Success.", ans, "are factors of", n)

if __name__ == "__main__":
    main(sys.argv[1:])