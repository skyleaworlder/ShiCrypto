name = "ECC"
help_info = '''
[ShiCrypto] You're using CLI-ECC, the following help info might be helpful:
            Usage.1 python ECC.py [<a>] [<b>] [<p>] -d
            eg. python ECC.py 1 6 11 -d

            Usage.2 python ECC.py [<a>] [<b>] [<p>] -a/--add [<point-str>] [<point-str>]
            need input str command param
            eg. python ECC.py 1 6 11 -a "(2,7)" "(2,7)"

            Usage.3 python ECC.py [<a>] [<b>] [<p>] -m/--mul/--multi [<point-str>] [<times>] [<choice>]
            need input str command param
            eg. python ECC.py 1 6 11 -m "(2,7)" 7
                python ECC.py 1 6 11 -m "(2,7)" 1100 --naf
'''

export_info = {
    "name": name,
    "help": help_info
}

import sys
from src.ECC import ECC

def main(argv):
    a,b,p = map(int, (argv[0],argv[1],argv[2]))
    ecc = ECC(a, b, p)

    if argv[3] == "-d" or argv[3] == "--dots":
        ecc.calcuDots()
        print(ecc.dots.__len__(), "dots are:", "( y^2 = x^3 +", ecc.a, "* x +", ecc.b,")")
        for index,dot in enumerate(ecc.dots):
            print(index, ":", dot)
    elif argv[3] == "-a" or argv[3] == "--add":
        P, Q = tuple(eval(argv[4])), tuple(eval(argv[5]))
        print(P, "+", Q, "=", ecc.add(P, Q))
    elif argv[3] == "-m" or argv[3] == "--mul" or argv[3] == "--multi":
        P = tuple(eval(argv[4]))
        k = int(argv[5])
        if argv.__len__() == 7 and argv[6] == "--naf":
            print(P, "*", k, "=", ecc.multi_NAF(P, k), "using NAF")
        else:
            print(P, "*", k, "=", ecc.multi(P, k))
    else:
        pass

if __name__ == "__main__":
    main(sys.argv[1:])
