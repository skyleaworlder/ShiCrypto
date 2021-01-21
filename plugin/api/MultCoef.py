name = "MultCoef"
help_info = '''
[ShiCrypto] You're using CLI-MultCoef, the following help info might be helpful:
            Usage: python MultCoef.py [<top-index>] -- [<bot-index-list>]
            eg. python MultCoef.py 64 -- 2 3 4 5 6 7 8 9 10 10
                python MultCoef.py 12 -- 5 7
'''

export_info = {
    "name": name,
    "help": help_info
}

import sys
from src.MultCoef import MultCoef

def main(argv):
    n = int(argv[0])
    k_arr = []

    flag = False
    for index,arg in enumerate(argv[1:]):
        if arg == "--":
            flag = True
        elif index > 0 and flag:
            k_arr.append(int(arg))
        else:
            pass
    else:
        assert k_arr.__len__() != 0

    obj = MultCoef(n, k_arr)
    obj.calcu()
    print("(", obj.n, "//", obj.k_arr, ") =", obj.res)

if __name__ == "__main__":
    main(sys.argv[1:])
