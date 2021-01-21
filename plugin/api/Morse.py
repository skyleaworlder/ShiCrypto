name = "Morse"
help_info = '''
[ShiCrypto] You're using CLI-Morse, the following help info might be helpful:
            eg. python Morse.py -e/--encode 456789
                python Morse.py -d/--decode ....- ..... -.... --... ---.. ----.
'''

export_info = {
    "name": name,
    "help": help_info
}

import sys
from src.Morse import enMorse, deMorse

def main(argv):
    arr = []
    if argv[0] == "-e" or argv[0] == "--encode":
        print("ciphertext:", enMorse(argv[1]))
    if argv[0] == "-d" or argv[0] == "--decode":
        arr = argv[1].split(" ") if type(argv[1]) is str else ""
        print("plaintext:", deMorse(arr))

if __name__ == "__main__":
    main(sys.argv[1:])
