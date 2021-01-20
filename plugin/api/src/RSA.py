from sympy import randprime
from random import randint
from Calcu import GCD, Inverse

class RSA:
    '''
    --null:         p,q gen_ed by randprime; a gen_ed by randint
    -pq:            p,q given by cmd params; a gen_ed by randint
    -pqa:           p,q,a given by cmd params

    private key:    p, q, a(decrypt key)
    public key:     n, phi, b(encrypt key)
    plain text:     x
    cipher text:    y
    '''
    def __init__(self, bit, opt='--null', p=None, q=None, a=None):
        if opt == '-pq' or opt == '-pqa':
            self.p = p
            self.q = q
        else:
            self.p = randprime(2**(bit-1), 2**bit)
            self.q = randprime(2**(bit-1), 2**bit)
        self.phi = (self.p-1)*(self.q-1)
        self.n = self.p * self.q

        if opt == '-pqa':
            self.a = a
        else:
            flag = True
            while flag:
                a_gen = randint(2**(2*bit-1), 2**(2*bit))
                if GCD(a_gen, self.phi) == 1:
                    flag = False
            self.a = a_gen
        self.b = Inverse(self.a, self.phi)

    def encrypt(self, x):
        return pow(x, self.b, self.n)

    def decrypt(self, y):
        return pow(y, self.a, self.n)
