'''
python Pohlig-Hellman.py [<n>] [<alpha>] [<beta>] [<q>] [<c>]
eg. python Pohlig-Hellman.py 28703 5 8563 28703 100
    python Pohlig-Hellman.py 31153 10 12611 31153 100
'''
import sys
from Calcu import Inverse, Mul

'''
x = a mod q^c
a = x + sq^c, s is a constant
n:      num given, alpha^a (mod n) should be beta
alpha:  public key
beta:   public key
q:      n can be desc_ed as pi_{i=1}^k q_i^{l_i}
c:      iter num
'''
def PohligHellman(n, alpha, beta, q, c):
    j = 0
    arr = []
    beta_j = beta
    while j <= c - 1:
        delta = pow(beta_j, (n // pow(q, j+1)), n)
        i = 0
        while delta != pow(alpha, ((i * n // q) % n), n):
            i = i + 1
        arr.append(i)
        ''' beta_{j+1} = beta_{j}*alpha^{-a_j*q^j} (mod n) '''
        beta_j = Mul(
            beta_j,
            pow(
                Inverse(alpha, n),
                Mul(arr[arr.__len__()-1], pow(q, j), n), n
            ), n
        )
        j = j + 1
    return arr

def main(argv):
    n, alpha, beta, q, c = map(int, (argv[0],argv[1],argv[2],argv[3],argv[4]))
    ans = PohligHellman(n, alpha, beta, q, c)

    print("About "+argv[1]+"^? = "+argv[2])
    print("The result in Z_{"+argv[0]+"} is:\n", ans)

if __name__ == "__main__":
    main(sys.argv[1:])
