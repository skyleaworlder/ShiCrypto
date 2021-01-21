name = "RSA"
help_info = '''
[ShiCrypto] You're using CLI-RSA, the following help info might be helpful:
            Usage.1 python RSA.py [<bit>] -pq [<p>] [<q>] [<plaintxt>]
            eg. python RSA.py 1024 -pq 17 65537 456

            Usage.2 python RSA.py [<bit>] -pqa [<p>] [<q>] [<a>] [<plaintxt>]
            eg. python RSA.py 512 -pqa 17 65537 789 456456

            Usage.3 python RSA.py [<bit>] --null [<plaintxt>]
            eg. python RSA.py 512 --null 123
'''

export_info = {
    "name": name,
    "help": help_info
}

import sys
from src.RSA import RSA

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
