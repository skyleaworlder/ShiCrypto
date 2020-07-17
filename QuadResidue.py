'''
1. python QuadResidue.py [<mode>] [<top-index>] [<bot-index>]
eg. python QuadResidue.py -l/--legendre 2 13
eg. python QuadResidue.py -j/--jacobi 2 26
'''
import sys
from PrimeTest import Fermat
from ConMod import DIVNum, DIVVerify
from math import sqrt, ceil
from functools import reduce

def legendre(a, p):
    if not Fermat(p):
        return -2
    ret = pow(a%p, (p-1)//2, p)
    return ret if ret == 1 else ret-p

def jacobi(a, n):
    if Fermat(n):
        return legendre(a, n)

    prime_arr = [i for i in range(2, ceil(sqrt(n))+1) if DIVVerify(i, n) and Fermat(i)]
    num_arr = [DIVNum(i, n) for i in prime_arr]
    index_arr = range(0, prime_arr.__len__())
    print(prime_arr, num_arr)
    return reduce(lambda x,index : x*pow(
            legendre(a, prime_arr[index]), num_arr[index]
        ), index_arr, 1)

def main(argv):
    if argv[0] == "-l" or argv[0] == "--legendre":
        print("("+argv[1]+"/"+argv[2]+") =", legendre(int(argv[1]), int(argv[2])))
    if argv[0] == "-j" or argv[0] == "--jacobi":
        print("("+argv[1]+"/"+argv[2]+") =", jacobi(int(argv[1]), int(argv[2])))

if __name__ == "__main__":
    main(sys.argv[1:])