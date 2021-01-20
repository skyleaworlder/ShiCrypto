'''
python ECIES.py [<a>] [<b>] [<p>] [<points-str>]
    [<m-private key>] [<n-prime>] [<plaintxt-num>]
eg. python ECIES.py 1 6 11 "(2,7)" 3 5 10
'''

import sys
from src.ECC import ECC
from src.ECIES import ECIES

def main(argv):
    a,b,p = map(int, (argv[0],argv[1],argv[2]))
    ecc = ECC(a, b, p)
    ecies = ECIES(
        E=ecc, P=tuple(eval(argv[3])),
        m=int(argv[4]), n=int(argv[5])
    )

    print(ecc.dots.__len__(), "dots in E are:")
    for index,dot in enumerate(ecc.dots):
        print(index, ":", dot)

    cipher = ecies.encrypt(int(argv[6]))
    print("cipher:")
    print("1. dot compressed:", cipher[0])
    print("2. number encrypted:", cipher[1])
    print("plaintxt:")
    print("your input is", ecies.decrypt(cipher))

if __name__ == "__main__":
    main(sys.argv[1:])
