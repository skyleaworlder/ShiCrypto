
'''
n is input to be tested
iterNum
'''
import sys
import random
from Calcu import GCD

def Fermat(n_i, iterNum_i=512):
    n = int(n_i)
    if n == 2 or n == 3:
        return True

    iterNum = int(iterNum_i)
    for i in range(0, iterNum):
        a = random.randint(2, n-2)
        if GCD(a, n) != 1:
            return False
        if pow(a, n-1, n) != 1:
            return False
    else:
        return True

def main(argv):
    if Fermat(argv[0], argv[1]):
        print(argv[0], "is a prime perhaps.")
    else:
        print(argv[0], "shouldn't be a prime.")

if __name__ == "__main__":
    main(sys.argv[1:])