import sys

def GCD(a, b):
    return a if b == 0 else GCD(b, a % b)

def EXgcd(a, b):
    q_arr = [0]
    while b != 0:
        q_arr.append(a // b)
        a, b = b, a % b
    return q_arr, a

def Inverse(a, n):
    q_arr, gcd = EXgcd(n, a)
    if gcd != 1:
        return -1
    else:
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
            t_arr.append((-1)**(i+1)*(abs(t_arr[i]) + q_arr[i+1] * abs(t_arr[i+1])))
        return t_arr[-1] % n # return the last elem in t_arr

def main(argv):
    if argv[0] == "--gcd" or argv[0] == '-g':
        print("gcd("+argv[1]+","+argv[2]+") = ", GCD(int(argv[1]), int(argv[2])))
    if argv[0] == "--rev" or argv[0] == '-r':
        print(argv[1]+"^{-1} mod "+argv[2]+" = ", Inverse(int(argv[1]), int(argv[2])))


if __name__ == "__main__":
    main(sys.argv[1:])