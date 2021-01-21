name = "Pohlig_Hellman"
help_info = '''
[ShiCrypto] You're using CLI-Pohlig_Hellman, the following help info might be helpful:
            Usage: python Pohlig-Hellman.py [<n>] [<alpha>] [<beta>] [<q>] [<c>]
            eg. python Pohlig-Hellman.py 28703 5 8563 28703 100
                python Pohlig-Hellman.py 31153 10 12611 31153 100
'''

export_info = {
    "name": name,
    "help": help_info
}

import sys
from src.Pohlig_Hellman import PohligHellman

def main(argv):
    n, alpha, beta, q, c = map(int, (argv[0],argv[1],argv[2],argv[3],argv[4]))
    ans = PohligHellman(n, alpha, beta, q, c)

    print("About "+argv[1]+"^? = "+argv[2])
    print("The result in Z_{"+argv[0]+"} is:\n", ans)

if __name__ == "__main__":
    main(sys.argv[1:])
