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
