'''
1. python RSA.py [<bit>] -pq [<p>] [<q>] [<plaintxt>]
2. python RSA.py [<bit>] -pqa [<p>] [<q>] [<a>] [<plaintxt>]
3. python RSA.py [<bit>] --null [<plaintxt>]

eg. python RSA.py 512 --null 123
'''
import sys
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

def main(argv):
    bit = int(argv[0])
    mode = argv[1]
    if mode == "-pqa":
        rsa = RSA(bit, opt=mode, p=int(argv[2]), q=int(argv[3]), a=int(argv[4]))
    elif mode == "-pq":
        rsa = RSA(bit, opt=mode, p=int(argv[2]), q=int(argv[3]))
    else:
        rsa = RSA(bit, opt=mode)

    print(
        "RSA-\""+str(2*bit)+"\" !",
        "\np is:", rsa.p, "\nq is:", rsa.q,
        "\nn is:", rsa.n, "\nphi is:", rsa.phi,
        "\na is:", rsa.a, "\nb is:", rsa.b, "\n"
    )
    cipher = rsa.encrypt(int(argv[-1]))
    print("plaintxt is:", argv[-1])
    print("ciphertxt is:", cipher)
    plaintxt = rsa.decrypt(cipher)
    print("plaintxt is (gain from ciphertxt):", plaintxt)

if __name__ == "__main__":
    main(sys.argv[1:])