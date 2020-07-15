import sys

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