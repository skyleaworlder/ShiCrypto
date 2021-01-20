'''
python Pollard_Rho_Log.py [<alpha>] [<beta>] [<modulo>]
eg. python Pollard_Rho_Log.py 2 5 98
    python Pollard_Rho_Log.py 3 12 5
    python Pollard_Rho_Log.py 11 980 12546
'''

import sys
from src.Pollard_Rho_Log import PollardRho

def main(argv):
    pr = PollardRho(int(argv[0]), int(argv[1]), int(argv[2]))
    res = pr.PollardRho()
    resstr = ""
    for elem in res:
        resstr += str(elem) + " "
    print("log_"+argv[0]+"("+argv[1]+") mod "+argv[2]+": "+resstr)

if __name__ == "__main__":
    main(sys.argv[1:])
