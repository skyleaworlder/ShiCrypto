'''
1. python QuadResidue.py [<mode>] [<top-index>] [<bot-index>]
eg. python QuadResidue.py -l/--legendre 2 13
eg. python QuadResidue.py -j/--jacobi 2 26
'''

import sys
from src.QuadResidue import legendre, jacobi

def main(argv):
    if argv[0] == "-l" or argv[0] == "--legendre":
        print("("+argv[1]+"/"+argv[2]+") =", legendre(int(argv[1]), int(argv[2])))
    if argv[0] == "-j" or argv[0] == "--jacobi":
        print("("+argv[1]+"/"+argv[2]+") =", jacobi(int(argv[1]), int(argv[2])))

if __name__ == "__main__":
    main(sys.argv[1:])
