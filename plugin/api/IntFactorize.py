'''
1. Pollard Rho
python IntFactorize.py --Rho/-r [<mode>] [<number>]
eg. python IntFactorize.py --Rho --origin 110
    python IntFactorize.py -r --nowadays 110

2. Fermat Factorization
python IntFactorize.py --Fermat/-f [<number>] [<iterNum>]
eg. python IntFactorize.py -f 11011 100
    python IntFactorize.py --Fermat 11 100

3. Wiener Attack
python IntFactorize.py --Wiener/-w [<number>] [<public-key-b>]
eg. python IntFactorize.py -w 160523347 60728973
    python IntFactorize.py --Wiener 160523347 60728981
'''

from ..src.IntFactorize import PollardRho, FermatFactor, WienerAttack

def main(argv):
    choice = argv[0]
    if choice == "--Rho" or choice == "-r":
        mode = argv[1]
        n = int(argv[2])
        rho = PollardRho(n)
        ans = rho.factoring(mode)
        if ans == -1:
            print("Failure.", n, "might be a prime.")
        else:
            print("Success:", n, "can be decomped to", ans, "and", n // ans)
    elif choice == "--Fermat" or choice == "-f":
        n = int(argv[1])
        iterNum = int(argv[2])
        ans = FermatFactor(n, iterNum)
        if ans == []:
            print("Failure.", n, "might be a prime, or try larger iterNum again.")
        else:
            print("Success.", ans, "are factors of", n)
    elif choice == "--Wiener" or choice == "-w":
        n = int(argv[1])
        b = int(argv[2])
        ans = WienerAttack(n, b)
        if ans == (-1, -1):
            print("Failure.", n, "cannot be factorized by this methods")
        else:
            print("Success.", ans, "are factors of", n)
