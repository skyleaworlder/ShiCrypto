'''
1. python QuadResidue.py [<mode>] [<top-index>] [<bot-index>]
eg. python QuadResidue.py -l/--legendre 2 13
eg. python QuadResidue.py -j/--jacobi 2 26
'''
import sys
from ConMod import DIVNum, DIVVerify
from math import sqrt, ceil
from functools import reduce

'''
p only can be odd prime
'''
def legendre(a, p):
    if a % p == 0:
        return 0
    else:
        ret = pow(a%p, (p-1)//2, p)
        return ret if ret == 1 else ret-p

def jacobi(a, n):
    if a == 1 or n == 1:
        return 1
    elif a == 0 or n % a == 0:
        return 0
    elif a == 2:
        return int(pow(-1, (n**2-1)/8))
    elif a == n-1:
        return int(pow(-1, (n-1)/2))
    elif a % 2 == 0:
        return jacobi(2, n) * jacobi(a//2, n)
    else:
        return int(pow(-1, (a-1)*(n-1)/4)) * jacobi(n%a, a)

def main(argv):
    if argv[0] == "-l" or argv[0] == "--legendre":
        print("("+argv[1]+"/"+argv[2]+") =", legendre(int(argv[1]), int(argv[2])))
    if argv[0] == "-j" or argv[0] == "--jacobi":
        print("("+argv[1]+"/"+argv[2]+") =", jacobi(int(argv[1]), int(argv[2])))

if __name__ == "__main__":
    main(sys.argv[1:])
