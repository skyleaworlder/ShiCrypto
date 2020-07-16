'''
python MultCoef.py [<top-index>] -- [<bot-index-list>]
eg. python MultCoef.py 64 -- 2 3 4 5 6 7 8 9 10 10
    python MultCoef.py 12 -- 5 7
'''
import sys
from functools import reduce
from math import factorial

class MultCoef:

    def __init__(self, n, k_arr):
        assert n == sum(k_arr)
        self.n = n
        self.k_arr = k_arr

    def calcu(self):
        k_fac_arr = [factorial(k) for k in self.k_arr]
        self.res = factorial(self.n) // reduce(lambda x,y : x*y, k_fac_arr, 1)

def main(argv):
    n = int(argv[0])
    k_arr = []

    flag = False
    for index,arg in enumerate(argv[1:]):
        if arg == "--":
            flag = True
        elif index > 0 and flag:
            k_arr.append(int(arg))
        else:
            pass
    else:
        assert k_arr.__len__() != 0

    obj = MultCoef(n, k_arr)
    obj.calcu()
    print("(", obj.n, "//", obj.k_arr, ") =", obj.res)

if __name__ == "__main__":
    main(sys.argv[1:])