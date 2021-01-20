'''
python CRT.py [<b-list>] -- [<m-list>]
eg. python CRT.py 1 2 -- 4 5
'''

import sys
from src.CRT import CRT

def main(argv):
    b_arr = []
    m_arr = []
    flag = 'b'
    for arg in argv:
        if arg == "--":
            flag = 'm'
            continue
        if flag == 'b':
            b_arr.append(int(arg))
        if flag == 'm':
            m_arr.append(int(arg))
    else:
        print("x =", CRT(b_arr, m_arr))

if __name__ == "__main__":
    main(sys.argv[1:])
