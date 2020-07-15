import sys
from PrimeTest import Fermat
from ConMod import DIVNum, DIVVerify
from math import sqrt, ceil
from functools import reduce

def legendre(a, p):
    return pow(a%p, (p-1)//2, p) if Fermat(p) else -2

def jacobin(a, n):
    if Fermat(n):
        return legendre(a, n)

    prime_arr = [i for i in range(2, ceil(sqrt(n))) if DIVVerify(i, n)]
    num_arr = [DIVNum(i, n) for i in prime_arr]
    index_arr = [i for i in range(0, prime_arr.__len__())]
    print(prime_arr, num_arr)
    return reduce(lambda x,index : x*pow(
            legendre(a, prime_arr[index]), num_arr[index]
        ), index_arr, 1)

def main(argv):
    if argv[0] == "-l" or argv[0] == "--legendre":
        print("("+argv[1]+"/"+argv[2]+") =", legendre(int(argv[1]), int(argv[2])))
    if argv[0] == "-j" or argv[0] == "--jacobin":
        print("("+argv[1]+"/"+argv[2]+") =", jacobin(int(argv[1]), int(argv[2])))

if __name__ == "__main__":
    main(sys.argv[1:])