name = "ElGamal"
help_info = '''
[ShiCrypto] You're using CLI-ElGamal, the following help info might be helpful:
            Usage: python ElGamal.py [<public-n>] [<public-alpha>] [<private-a>] [<plaintxt>]
            eg. python ElGamal.py 101 11 45 46
                python ElGamal.py 101 10 45 46
'''

export_info = {
    "name": name,
    "help": help_info
}

import sys
from src.ElGamal import ElGamal

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
