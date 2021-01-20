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
