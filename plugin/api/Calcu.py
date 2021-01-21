name = "Calcu"
help_info = '''
[ShiCrypto] You're using CLI-Calcu, the following help info might be helpful:
            Usage.1: python Calcu.py [<choice>] [<op1>] [<op2>] [<modulo>]
            add / sub / mul / div are in choices.
            eg. python Calcu.py --add/-a 5 6 12
                python Calcu.py --sub/-s 5 6 12
                python Calcu.py --mul/-m 5 5 12
                python Calcu.py --div/-d 2 6 12

            Usage.2: python Calcu.py [<choice>] [<op1>] [<op2>]
            gcd / lcm / exculid(process) are in choices.
            eg. python Calcu.py --gcd/-g 7 5
                python Calcu.py --lcm/-l 4 6
                python Calcu.py --exeuclid/-ex 13 64

            Usage.3: python Calcu.py [<choice>] [<op>] [<modulo>]
            inv(inverse), sqrt are in choices.
            eg. python Calcu.py --inv/-i 62 12
                python Calcu.py --sqrt 5 11

            Usage.4: python Calcu.py [<choice>] [<op>]
            euler(function) is in choices.
            eg. python Calcu.py --euler/-e 14
'''

export_info = {
    "name": name,
    "help": help_info
}

import sys
from src.Calcu import *

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
