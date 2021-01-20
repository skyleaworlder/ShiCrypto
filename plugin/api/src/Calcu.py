import sys
from math import ceil

def Add(a, b, n):
    return (a + b) % n

def Sub(a, b, n):
    return (a - b) % n

def Mul(a, b, n):
    return (a * b) % n

def GCD(a, b):
    return a if b == 0 else GCD(b, a % b)

def LCM(a, b):
    return a*b // GCD(a, b)

def EXgcd(a, b):
    q_arr = [0]
    while b != 0:
        q_arr.append(a // b)
        a, b = b, a % b
    return q_arr, a

def EXeuclid(a, b):
    ''' b > a normally '''
    q_arr, gcd = EXgcd(b, a)
    s_arr = [1, 0]
    t_arr = [0, 1]
    '''
    if r_n == 1, q_arr.len == n.
    cos t_n = t_{n-2} + q_{n-1} * t_{n-1}
        then q_arr do not need q_n
        then iterNum = (q-1) - 1
    '''
    iterNum = q_arr.__len__() - 2
    for i in range(0, iterNum):
        ''' t_n = t_{n-2} + q_{n-1} * t_{n-1} '''
        ''' s_n = s_{n-2} + q_{n-1} * s_{n-1} '''
        s_arr.append((-1)**(i)*(abs(s_arr[i]) + q_arr[i+1] * abs(s_arr[i+1])))
        t_arr.append((-1)**(i+1)*(abs(t_arr[i]) + q_arr[i+1] * abs(t_arr[i+1])))
    return s_arr[-1], t_arr[-1], gcd

def Inverse(a, n):
    s, t, gcd = EXeuclid(a, n)
    if gcd != 1:
        return -1
    else:
        return t % n # return the last elem in t_arr

def Div(a, b, p):
    b_inv = Inverse(b, p)
    assert b_inv != -1
    return Mul(a, Inverse(b, p), p)

def Sqrt(z, n):
    for i in range(0, int(ceil((n+1) / 2))):
        if pow(i, 2, n) == (z%n):
            return [i, n - i]
    else:
        return [-1, -1]

def Euler(n):
    cnt = 0
    for i in range(1, n):
        cnt += 1 if GCD(n, i) == 1 else 0
    return cnt
