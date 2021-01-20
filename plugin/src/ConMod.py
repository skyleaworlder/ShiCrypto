import sys
from Calcu import GCD, Inverse, Mul

def CMVerify(a, b, n):
    return (a%n == b%n)

def DIVVerify(a, b):
    return (b%a == 0) and (a!=0)

def DIVNum(a, b):
    cnt = 0
    while DIVVerify(a, b):
        b = b // a
        cnt += 1
    return cnt

def CongEq(a, b, n):
    d = GCD(a, n)
    if d != 1 and not DIVVerify(d, b):
        return [-1]
    elif d != 1:
        res =  CongEq(a//d, b//d, n//d)
        k = 1
        while k*n//d < n:
            res.append(res[0] + k*n//d)
            k += 1
        return res
    else:
        return [Mul(b, Inverse(a, n), n)]
