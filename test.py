from plugin.api import Calcu, continued, CRT, QuadResidue, PrimeTest, Pohlig_Hellman, Pollard_Rho_Log, MultCoef, IntFactorize, RSA, Shanks, ECC, ECIES, ElGamal, Morse
import sys
from ddt import ddt, data, unpack
import unittest

@ddt
class Test(unittest.TestCase):

    Calcu_data = [
        ("--add", "5", "6", "12"),
        ("--sub", "5", "6", "12"),
    ]
    @data(Calcu_data)
    @unpack
    def test_Calcu(self, *args, **kwargs):
        print("1.Calcu:")
        for data in args:
            Calcu.main(data)

    continued_data = [
        ("17", "45", "4"),
        ("17", "45", "6"),
    ]
    @data(continued_data)
    @unpack
    def test_continued(self, *args, **kwargs):
        print("2.continued:")
        for data in args:
            continued.main(data)

    CRT_data = [
        ("1", "2", "--", "4", "5"),
    ]
    @data(CRT_data)
    @unpack
    def test_CRT(self, *args, **kwargs):
        print("3.CRT:")
        for data in args:
            CRT.main(data)

    QuadResidue_data = [
        ("-l", "2", "13"),
        ("--jacobi", "2", "26"),
    ]
    @data(QuadResidue_data)
    @unpack
    def test_QuadResidue(self, *args, **kwargs):
        print("4.QuadResidue:")
        for data in args:
            QuadResidue.main(data)

    PrimeTest_data = [
        ("-m", "64", "12"),
        ("--Fermat", "65", "12"),
        ("-t", "128"),
    ]
    @data(PrimeTest_data)
    @unpack
    def test_PrimeTest(self, *args, **kwargs):
        print("5.PrimeTest:")
        for data in args:
            PrimeTest.main(data)

    Pohlig_Hellman_data = [
        ("28703", "5", "8563", "28703", "100"),
        ("31153", "10", "12611", "31153", "100"),
    ]
    @data(Pohlig_Hellman_data)
    @unpack
    def test_Pohlig_Hellman(self, *args, **kwargs):
        print("6.Pohlig Hellman Test:")
        for data in args:
            Pohlig_Hellman.main(data)

    Pollard_Rho_Log_data = [
        ("2", "5", "98"),
        ("3", "12", "5"),
        ("11", "980", "12546"),
    ]
    @data(Pollard_Rho_Log_data)
    @unpack
    def test_Pollard_Rho_Log(self, *args, **kwargs):
        print("7.Pollard-Rho-Log Test:")
        for data in args:
            Pollard_Rho_Log.main(data)

    MultCoef_data = [
        ("64", "--", "2", "3", "4", "5", "6", "7", "8", "9", "10", "10"),
        ("12", "--", "5", "7"),
        ("4", "--", "3", "1"),
    ]
    @data(MultCoef_data)
    @unpack
    def test_MultCoef(self, *args, **kwargs):
        print("8.MultCoef Test:")
        for data in args:
            MultCoef.main(data)

    IntFactorize_data = [
        ("--Rho", "--origin", "110"),
        ("-r", "--nowadays", "110"),
        ("--Fermat", "11011", "100"),
        ("-f", "11", "100"),
        ("-w", "160523347", "60728973"),
        ("--Wiener", "160523347", "60728973"),
    ]
    @data(IntFactorize_data)
    @unpack
    def test_IntFactorize(self, *args, **kwargs):
        print("9.IntFactorize Test:")
        for data in args:
            IntFactorize.main(data)

    RSA_data = [
        ("512", "--null", "123"),
        ("1024", "-pq", "17", "65537", "123"),
    ]
    @data(RSA_data)
    @unpack
    def test_RSA(self, *args, **kwargs):
        print("10.RSA Test:")
        for data in args:
            RSA.main(data)

    Shanks_data = [
        ("121", "13", "5"),
        ("41", "12", "7"),
        ("121", "3", "5"),
    ]
    @data(Shanks_data)
    @unpack
    def test_Shanks(self, *args, **kwargs):
        print("11.Shanks Test:")
        for data in args:
            Shanks.main(data)

    ECC_data = [
        ("1", "6", "11", "-d"),
        ("1", "6", "11", "-a", "(2,7)", "(2,7)"),
        ("1", "6", "11", "-m", "(2,7)", "7"),
        ("1", "6", "11", "-m", "(2,7)", "1100", "--naf"),
    ]
    @data(ECC_data)
    @unpack
    def test_ECC(self, *args, **kwargs):
        print("12.ECC Test:")
        for data in args:
            ECC.main(data)

    ECIES_data = [
        ("1", "6", "11", "(2,7)", "3", "5", "10"),
    ]
    @data(ECIES_data)
    @unpack
    def test_ECIES(self, *args, **kwargs):
        print("13.ECIES Test:")
        for data in args:
            ECIES.main(data)

    ElGamal_data = [
        ("101", "11", "45", "46"),
        ("101", "10", "45", "46"),
    ]
    @data(ElGamal_data)
    @unpack
    def test_ElGamal(self, *args, **kwargs):
        print("14.ElGamal Test:")
        for data in args:
            ElGamal.main(data)

    Morse_data = [
        ("-e", "456789"),
        ("--decode", "....- ..... -.... --... ---.. ----."),
    ]
    @data(Morse_data)
    @unpack
    def test_Morse(self, *args, **kwargs):
        print("15.Morse Test:")
        for data in args:
            Morse.main(data)

if __name__ == "__main__":
    unittest.main()
