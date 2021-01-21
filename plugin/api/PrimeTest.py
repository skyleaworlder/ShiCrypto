name = "PrimeTest"
help_info = '''
[ShiCrypto] You're using CLI-PrimeTest, the following help info might be helpful:
            Usage: python PrimeTest.py [<choice>] [<test-num>] [<iter-num>]
            eg. python PrimeTest.py -m/--Miller-Rabin 64 12
                python PrimeTest.py -f/--Fermat 65 12
                python PrimeTest.py -t/--Trial 128
'''

export_info = {
    "name": name,
    "help": help_info
}

import sys
from src.PrimeTest import MillerRabin, Fermat, Trial, SolovayStrassen

def main(argv):
    if argv[0] == "-m" or argv[0] == "--Miller-Rabin":
        flag = MillerRabin(int(argv[1]), int(argv[2]))
        print("using Miller-Rabin prime test:")
    elif argv[0] == "-f" or argv[0] == "--Fermat":
        print("using Fermat prime test:")
        flag = Fermat(int(argv[1]), int(argv[2]))
    elif argv[0] == "-t" or argv[0] == "--Trial":
        print("using Trial test:")
        flag = Trial(int(argv[1]))
    elif argv[0] == "-s" or argv[0] == "--Solovay-Strassen":
        print("using Solovay-Strassen prime test:")
        flag = SolovayStrassen(int(argv[1]), int(argv[2]))

    if flag:
        print(argv[1], "is a prime perhaps.")
    else:
        print(argv[1], "shouldn't be a prime.")

if __name__ == "__main__":
    main(sys.argv[1:])
