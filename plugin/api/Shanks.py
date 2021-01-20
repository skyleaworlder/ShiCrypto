'''
python Shanks.py [<modulo>] [<alpha>] [<beta>]
eg. python Shanks.py 121 13 5
    python Shanks.py 41 12 7
    python Shanks.py 121 3 5
the first and second success, while the third one failed
'''

import sys
from src.Shanks import Shanks

def main(argv):
    n, alpha, beta = map(int, (argv[0], argv[1], argv[2]))
    a = Shanks(n, alpha, beta)
    print("To find a, st."+argv[1]+"^a = "+argv[2])
    if a != -1 and pow(alpha, a, n) == beta:
        print("Success:", argv[1]+"^"+str(a)+" = "+argv[2])
    else:
        print("Failed")

if __name__ == "__main__":
    main(sys.argv[1:])
