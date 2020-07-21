'''
python ElGamal.py [<public-n>] [<public-alpha>] [<private-a>] [<plaintxt>]
eg. python ElGamal.py 101 11 45 46
    python ElGamal.py 101 10 45 46
'''
import sys
import random
from Calcu import Mul, Inverse

class ElGamal:

    '''
    public key:     n, alpha, beta
    private key:    a, k(random number)
    plain text:     x
    cipher text:    y_1, y_2
    '''
    def __init__(self, n):
        self.n = n

    def generate(self, alpha, a):
        assert a < self.n and alpha < self.n
        self.alpha = alpha
        self.a = a
        self.beta = pow(self.alpha, self.a, self.n)
        self.k = random.randint(1, self.n-1)

    def encrypt(self, x):
        return (
            pow(self.alpha, self.k, self.n),
            Mul(x, pow(self.beta, self.k, self.n), self.n)
        )

    def decrypt(self, y_1, y_2):
        return Mul(
            y_2,
            Inverse(pow(y_1, self.a, self.n), self.n),
            self.n
        )

def main(argv):
    n = int(argv[0])
    alpha = int(argv[1])
    a = int(argv[2])

    elg = ElGamal(n)
    elg.generate(alpha, a)
    print("ElGamal public key:")
    print("n:", n, "alpha:", alpha, "beta", elg.beta, "\n")
    print("ElGamal private key(a):", a, "\n")

    ciphertxt = elg.encrypt(int(argv[3]))
    print("ciphertxt is", ciphertxt)
    print("y_1 is", ciphertxt[0], "and y_2 is", ciphertxt[1], "\n")
    plaintxt = elg.decrypt(ciphertxt[0], ciphertxt[1])
    print("plaintxt is", plaintxt)

if __name__ == "__main__":
    main(sys.argv[1:])