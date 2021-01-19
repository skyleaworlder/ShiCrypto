'''
python Shanks.py [<modulo>] [<alpha>] [<beta>]
eg. python Shanks.py 121 13 5
    python Shanks.py 41 12 7
    python Shanks.py 121 3 5
the first and second success, while the third one failed
'''
import sys
from math import ceil, sqrt
from Calcu import Inverse, Mul, Add

def Shanks(n, alpha, beta):
    m = int(ceil(sqrt(n)))

    j_alpha = [
        {   "j": j,
            "alpha^jm": pow(alpha, j*m, n)
        } for j in range(0, m)
    ]
    j_alpha.sort(key=lambda item : item["alpha^jm"])

    i_ba_inv = [
        {   "i": i,
            "beta*alpha^-i": Mul(
                beta,
                Inverse(pow(alpha, i, n), n),
                n
        )} for i in range(0, m)
    ]
    i_ba_inv.sort(key=lambda item : item["beta*alpha^-i"])

    '''
    move index and jndex
    to find which i, j st. alpha^jm = beta*alpha^-i
    '''
    index,jndex = 0,0
    while index != m and jndex != m:
        if j_alpha[jndex]["alpha^jm"] > i_ba_inv[index]["beta*alpha^-i"]:
            index += 1
        elif j_alpha[jndex]["alpha^jm"] < i_ba_inv[index]["beta*alpha^-i"]:
            jndex += 1
        else:
            return Add(m*j_alpha[jndex]["j"], i_ba_inv[index]["i"], n)
    return -1

def main(argv):
    n, alpha, beta = map(int, (argv[0], argv[1], argv[2]))
    a = Shanks(n, alpha, beta)
    print("To find a, st."+argv[1]+"^a = "+argv[2])
    if a != -1 and pow(alpha, a, n) == beta:
        print("Success:", argv[1]+"^"+str(a)+" = "+argv[2])
    else:
        print("Failed")

if __name__ == "__main__":
    main(sys.argv[1:])
