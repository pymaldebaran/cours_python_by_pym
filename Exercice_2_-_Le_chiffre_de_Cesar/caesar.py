#! /usr/bin/env python3
"""
Solution de l'exercice 2 tel que définit dans
[l'énoncé de l'exercice 2](README.md).
"""
import string
import logging
import sys
from typing import Dict

class Colors:
    """Colored prints
    """

    NC = "\033[0m"
    RED = "\033[31m"


def logging_print(message: str, type_loging: logging):
    """create logs
    """
    type_loging(message)
    
def create_transtab(key: int) -> str:
    """return the transtab

    the transtab is a dict which can bu used with translate method in order to transform a string into a cypher string
    """
    TRUE_ALPHABET = string.ascii_uppercase
    Z_UPPER_ASCII = 90
    A_UPPER_ASCII = 65
    AJUSTMENT = 1  # make ajustment in order to take the last or the first letter
    if A_UPPER_ASCII + key >= A_UPPER_ASCII:
        begining_cypher_alphabet = A_UPPER_ASCII + key
    else:
        begining_cypher_alphabet = Z_UPPER_ASCII + key + AJUSTMENT
    if Z_UPPER_ASCII + key <= Z_UPPER_ASCII:
        ending_cypher_alphabet = Z_UPPER_ASCII + key
    else:
        ending_cypher_alphabet = A_UPPER_ASCII + key - AJUSTMENT

    cypher_alphabet_begin_to_Z = list(
        map(chr, range(begining_cypher_alphabet, Z_UPPER_ASCII + AJUSTMENT))
    )
    cypher_alphabet_Z_to_ending = list(
        map(chr, range(A_UPPER_ASCII, ending_cypher_alphabet + AJUSTMENT))
    )
    cypher_alphabet = "".join(cypher_alphabet_begin_to_Z) + "".join(
        cypher_alphabet_Z_to_ending
    )

    transtab = str.maketrans(TRUE_ALPHABET, cypher_alphabet)
    return transtab

def do_cipher(plain_text: str, key: int) -> str:
    """Cipher a string object with the given key"""
    if key > 26 or key < -26:
        logging_print(
            f"{Colors.RED}Need to have a key between -26 and 26{Colors.NC}",
            logging.error,
        )
        sys.exit()

    plain_text_upper = plain_text.upper()
    transtab = create_transtab(key)
    cypher_text = plain_text_upper.translate(transtab)

    return cypher_text

  
def do_decipher(cipher_text: str, key: int) -> str:
    """Decipher a string object with the given key"""
    counter_key = -key
    transtab = create_transtab(counter_key)
    decipher_text = cipher_text.translate(transtab)
    return decipher_text


def exercise_2_1():
    PLAIN_TEXT = "Ave Caesar morituri te salutant"
    KEY = 3

    print("************* Exercise  2.1 *************\n\n")
    print("************ Caesar's cypher ************\n\n")
    print("Plain text   :", PLAIN_TEXT)
    print("key          :", KEY)
    print()

    print("Let's cipher now!")
    CIPHER_TEXT = do_cipher(PLAIN_TEXT, KEY)
    print("Cipher text  :", CIPHER_TEXT)
    print()

    print("Let's decipher (will it work?!)")
    DECIPHER_TEXT = do_decipher(CIPHER_TEXT, KEY)
    print("Decipher text:", DECIPHER_TEXT)
    print()

    SUCCESS = PLAIN_TEXT.upper() == DECIPHER_TEXT
    print("Did it worked?", "OK :)" if SUCCESS else "Nope :(")


def letter_frequency(cypher_text: str) -> Dict[str, int]:
    # Met ton code ici
    return {}


def crack_key(cypher_text: str) -> int:
    # Met ton code ici
    return 0


def exercise_2_2():
    INTERCEPTED_TEXT = "KPIVKM L'MABIQVO : "
    "RMCVM LMUWVMBBM, MTTM I CVM IXXIZMVKM PCUIQVM, UIQA LWBMM "
    "LM LMCF XMBQBMA KWZVMA ACZ TM NZWVB MB LM LMCF IQTMA LMUWVQIYCMA, "
    "BGXM KPICDM-AWCZQA, LIVA TM LWA. UITOZM AMA IQTMA, MTTM VM AIQB YCM "
    "XTIVMZ. LCZIVB TMCZA WXMZIBQWVA, MTTM I XWCZ VWU LM KWLM JTIKSJQZL."

    EXPECTED_TEXT = "Chance d'Estaing : "
    "Jeune demonette, elle a une apparence humaine, mais dotee "
    "de deux petites cornes sur le front et de deux ailes demoniaques, "
    "type chauve-souris, dans le dos. Malgre ses ailes, elle ne sait que "
    "planer. Durant leurs operations, elle a pour nom de code Blackbird."

    print("************* Exercise  2.2 *************\n\n")
    print("****** Let's break Caesar's cypher ******\n\n")
    print("Intercepted text    :", INTERCEPTED_TEXT)
    print("Expacted clear text :", EXPECTED_TEXT)
    print("Key                 :", "???")
    print()

    print("Let's break it")
    CRACKED_KEY = crack_key(INTERCEPTED_TEXT)
    print("Cracked key      :", CRACKED_KEY)
    print()

    print("Let's use the cracked key (will it work?!)")
    CRACKED_TEXT = do_decipher(INTERCEPTED_TEXT, CRACKED_KEY)
    print("Cracked text:", CRACKED_TEXT)
    print()

    SUCCESS = EXPECTED_TEXT.upper() == CRACKED_TEXT
    print("Did it worked?", "OK :)" if SUCCESS else "Nope :(")


def main():
    exercise_2_1()

    print()
    print()

    exercise_2_2()


if __name__ == "__main__":
    main()
