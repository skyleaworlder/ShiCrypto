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
