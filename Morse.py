import sys
from functools import reduce

MorseCB_de = {
    ".-":"A", "-...":"B", "-.-.":"C", "-..":"D", ".":"E", "..-.":"F",
    "--.":"G", "....":"H", "..":"I", ".---":"J", "-.-":"K", ".-..":"L",
    "--":"M", "-.":"N", "---":"O", ".--.":"P", "--.-":"Q", ".-.":"R",
    "...":"S", "-":"T", "..-":"U", "...-":"V", ".--":"W", "-..-":"X",
    "-.--":"Y", "--..":"Z",

    ".----":"1", "..---":"2", "...--":"3", "....-":"4", ".....":"5",
    "-....":"6", "--...":"7", "---..":"8", "----.":"9", "-----":"0",
}

MorseCB_en = {
    "A":".-", "B":"-...", "C":"-.-.", "D":"-..", "E":".", "F":"..-.",
    "G":"--.", "H":"....", "I":"..", "J":".---", "K":"-.-", "L":".-..",
    "M":"--", "N":"-.", "O":"---", "P":".--.", "Q":"--.-", "R":".-.",
    "S":"...", "T":"-", "U":"..-", "V":"...-", "W":".--", "X":"-..-",
    "Y":"-.--", "Z":"--..",

    "1":".----", "2":"..---", "3":"...--", "4":"....-", "5":".....",
    "6":"-....", "7":"--...", "8":"---..", "9":"----.", "0":"-----",
}

def _deMorse(cipher_arr):
    return reduce(lambda x,y : x+MorseCB_de[y], cipher_arr, "")

def _enMorse(plain_arr):
    return reduce(lambda x,y : x+MorseCB_en[y]+" ", plain_arr, "")

def main(argv):
    arr = []
    if argv[0] == "-e" or argv[0] == "--encode":
        print("ciphertext:", _enMorse(argv[1]))
    if argv[0] == "-d" or argv[0] == "--decode":
        arr = argv[1].split(" ") if type(argv[1]) is str else ""
        print("plaintext:", _deMorse(arr))

if __name__ == "__main__":
    main(sys.argv[1:])
