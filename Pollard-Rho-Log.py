'''
python Pollard-Rho-Log.py [<alpha>] [<beta>] [<modulo>]
eg. python Pollard-Rho-Log.py 2 5 98
    python Pollard-Rho-Log.py 3 12 5
    python Pollard-Rho-Log.py 11 980 12546
'''
import sys
from ConMod import CMVerify, CongEq
from Calcu import GCD, Mul, Add, Inverse, Sub
from Primitive import elemOrder

'''
alpha^a = beta (mod n)
'''
class PollardRho:

    def __init__(self, alpha, beta, n):
        self.alpha = alpha
        self.beta = beta
        self.n = n
        self.ord = elemOrder(self.alpha, self.n)
        '''
        elem in finite group can have infinite order
        such as 2 in { 0, 1, 2, 3 }
        '''
        assert self.ord != float('inf')

        self.S1 = []
        self.S2 = []
        self.S3 = []
        for i in range(0, n):
            if CMVerify(i, 2, 3):
                self.S1.append(i)
            elif CMVerify(i, 0, 3):
                self.S2.append(i)
            else:
                self.S3.append(i)

    def _fx(self, x, a, b):
        if x in self.S1:
            return (
                Mul(self.beta, x, self.n),
                a,
                Add(b, 1, self.ord)
            )
        elif x in self.S2:
            return (
                pow(x, 2, self.n),
                Mul(2, a, self.ord),
                Mul(2, b, self.ord)
            )
        else:
            return (
                Mul(self.alpha, x, self.n),
                Add(a, 1, self.ord),
                b
            )

    def PollardRho(self):
        x, a, b  = self._fx(1,0,0)
        x_,a_,b_ = self._fx(x,a,b)
        while x != x_:
            x, a, b  = self._fx(x, a, b)
            x_,a_,b_ = self._fx(x_, a_, b_)
            x_,a_,b_ = self._fx(x_, a_, b_)

        if GCD(b_-b, self.n) != 1:
            return [-1]
        else:
            '''
            using CongEq instead of Mul(a-a_, Inv(b_-b))
            cos congruence equation can have several solutions probably
            '''
            return CongEq(
                Sub(b_, b, self.ord),
                Sub(a, a_, self.ord),
                self.ord
            )

def main(argv):
    pr = PollardRho(int(argv[0]), int(argv[1]), int(argv[2]))
    res = pr.PollardRho()
    resstr = ""
    for elem in res:
        resstr += str(elem) + " "
    print("log_"+argv[0]+"("+argv[1]+") mod "+argv[2]+": "+resstr)

if __name__ == "__main__":
    main(sys.argv[1:])
