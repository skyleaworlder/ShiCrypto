'''
python PrimeTest.py [<choice>] [<test-num>] [<iter-num>]
eg. python PrimeTest.py -m/--Miller-Rabin 64 12
    python PrimeTest.py -f/--Fermat 65 12
    python PrimeTest.py -t/--Trial 128
'''
import sys
import random
from Calcu import GCD
from ConMod import DIVNum, CMVerify
from sympy import prime, nextprime
from math import ceil, sqrt
from QuadResidue import jacobi

'''
n is input to be tested
iterNum
'''
def Fermat(n, iterNum=512):
    if n == 2 or n == 3:
        return True

    for i in range(0, iterNum):
        a = random.randint(2, n-2)
        if GCD(a, n) != 1:
            return False
        if pow(a, n-1, n) != 1:
            return False
    else:
        return True

def Trial(n):
    p = prime(1)
    bound = ceil(sqrt(n))
    while p < bound:
        if n % p == 0:
            return False
        p = nextprime(p)
    return True

def MillerRabin(n, iterNum=512):
    r = DIVNum(2, n-1)
    d = (n-1) // pow(2,r)

    cnt = 0
    while cnt < iterNum:
        a = random.randint(2, n)
        if pow(a, d, n) == 1 or pow(a, d, n) == n-1:
            return True

        r_0 = 0
        while r_0 < r:
            if pow(a, pow(2,r_0)*d, n) == n-1:
                return True
            r_0 += 1
        cnt += 1

    return False

def SolovayStrassen(n, iterNum=512):
    cnt = 0
    while cnt < iterNum:
        a = random.randint(1, n-1)
        x = jacobi(a, n)
        if x == 0:
            return False
        else:
            y = pow(a, (n-1)//2, n)
            if CMVerify(x, y, n) == False:
                return False
        cnt += 1
    return True

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
