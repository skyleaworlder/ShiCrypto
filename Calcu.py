'''
eg. python Calcu.py --add/-a 5 6 12
    python Calcu.py --sub/-s 5 6 12
    python Calcu.py --mul/-m 5 5 12
    python Calcu.py --gcd/-g 7 5
    python Calcu.py --lcm/-l 4 6
    python Calcu.py --exeuclid/-ex 13 64
    python Calcu.py --inv/-i 62 12
    python Calcu.py --div/-d 2 6 12
    python Calcu.py --sqrt 5 11
    python Calcu.py --euler/-e 14
'''
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

def main(argv):
    if argv[0] == "--add" or argv[0] == "-a":
        print(argv[1]+"+"+argv[2]+" mod "+argv[3]+" =", Add(int(argv[1]), int(argv[2]), int(argv[3])))
    if argv[0] == "--sub" or argv[0] == "-s":
        print(argv[1]+"-"+argv[2]+" mod "+argv[3]+" =", Sub(int(argv[1]), int(argv[2]), int(argv[3])))
    if argv[0] == "--mul" or argv[0] == "-m":
        print(argv[1]+"*"+argv[2]+" mod "+argv[3]+" =", Mul(int(argv[1]), int(argv[2]), int(argv[3])))
    if argv[0] == "--gcd" or argv[0] == '-g':
        print("gcd("+argv[1]+","+argv[2]+") = ", GCD(int(argv[1]), int(argv[2])))
    if argv[0] == "--lcm" or argv[0] == "-l":
        print("lcm("+argv[1]+","+argv[2]+") = ", LCM(int(argv[1]), int(argv[2])))
    if argv[0] == "--exeuclid" or argv[0] == "-ex":
        s, t, gcd = EXeuclid(int(argv[1]), int(argv[2]))
        print(str(t)+"*"+argv[1]+" + "+str(s)+"*"+argv[2]+" =", gcd)
    if argv[0] == "--inv" or argv[0] == '-i':
        print(argv[1]+"^{-1} mod "+argv[2]+" = ", Inverse(int(argv[1]), int(argv[2])))
    if argv[0] == "--div" or argv[0] == "-d":
        print(argv[1]+"/"+argv[2]+" mod "+argv[3]+" =", Div(int(argv[1]), int(argv[2]), int(argv[3])))
    if argv[0] == "--sqrt":
        res = Sqrt(int(argv[1]), int(argv[2]))
        print("sqrt("+argv[1]+") mod "+argv[2]+" = ", res[0], " and ", res[1])
    if argv[0] == "--euler" or argv[0] == "-e":
        print("Phi("+argv[1]+") =", Euler(int(argv[1])))

if __name__ == "__main__":
    main(sys.argv[1:])
