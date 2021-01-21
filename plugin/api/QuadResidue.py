name = "QuadResidue"
help_info = '''
[ShiCrypto] You're using CLI-QuadResidue, the following help info might be helpful:
            Usage: python QuadResidue.py [<mode>] [<top-index>] [<bot-index>]
            eg. python QuadResidue.py -l/--legendre 2 13
                python QuadResidue.py -j/--jacobi 2 26
'''

export_info = {
    "name": name,
    "help": help_info
}

import sys
from src.QuadResidue import legendre, jacobi

def main(argv):
    if argv[0] == "-l" or argv[0] == "--legendre":
        print("("+argv[1]+"/"+argv[2]+") =", legendre(int(argv[1]), int(argv[2])))
    if argv[0] == "-j" or argv[0] == "--jacobi":
        print("("+argv[1]+"/"+argv[2]+") =", jacobi(int(argv[1]), int(argv[2])))

if __name__ == "__main__":
    main(sys.argv[1:])
