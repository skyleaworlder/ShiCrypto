from plugin.api import CRT, Calcu, continued, ECC, ECIES, ElGamal
from plugin.api import IntFactorize, Morse, MultCoef, Pohlig_Hellman
from plugin.api import Pollard_Rho_Log, PrimeTest, QuadResidue, RSA, Shanks

import sys

logo = '''
================================================================
                                                By skyleaworlder
  ________.__    ._________                        __
 /   ____/|  |__ |__\_ ___ \_______ ___.__._______/  |_  ____
 \____  \ |  |  \|  /  \  \/\_  __ <   |  |\____ \   __\/  _ )
 /       \|   Y  \  \   \____|  | \/\___  ||  |_> >  | (  <_> )
/______  /|___|  /__|\____  /|__|   / ____||   __/|__|  \____/
       \/      \/         \/        \/     |__|
================================================================
'''

print logo

pkg_lst = [
    CRT, Calcu, continued, ECC, ECIES, ElGamal,
    IntFactorize, Morse, MultCoef, Pohlig_Hellman,
    Pollard_Rho_Log, PrimeTest, QuadResidue, RSA, Shanks
]

def CLI():
    print "[ShiCrypto] The followings are supported well perhaps..."
    for i, pkg in enumerate(pkg_lst):
        print "{:>5s}, {:<15s}".format(str(i), pkg.export_info["name"]),
        if (i+1) % 3 == 0:
            print ' '

    while True:
        choice = raw_input("[ShiCrypto] Your choice is: ")
        if int(choice) in range(len(pkg_lst)):
            break
        else:
            print "[ShiCrypto] Your choice aren't supported."

    print pkg_lst[int(choice)].export_info["help"]
    print "[ShiCrypto] Your choice is", choice+".", pkg_lst[int(choice)].export_info["name"]+"."
    print "[ShiCrypto] It has to be NOTICED that \"python XXX.py \" aren't included in ARGV you input."
    print "            eg. if \"python Calcu.py --add 4 5 9\", your \"argv\" should be \"--add 4 5 9\"."

    argv = raw_input("Please input your \"argv\": ")
    argv = tuple(argv.split(" "))

    pkg_lst[int(choice)].main(argv)

    return

if __name__ == "__main__":
    CLI()
