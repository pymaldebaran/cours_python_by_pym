#! /usr/bin/env python3
"""
Solution de l'exercice 2 tel que définit dans
[l'énoncé de l'exercice 2](README.md).
"""

from typing import Dict
import string


def shift(container: str, amount: int) -> str:
    """Shift container by amount (put back at the start outside shifted elements from the end)."""
    new_start = amount % len(container)
    return container[new_start:] + container[:new_start]


def do_cipher(plain_text: str, key: int) -> str:
    """
    Cipher plain text from caesar encryption key.
    Treat insensitive-case input plain text and output ciphered text upper cased.
    """
    plain_text_upper = plain_text.upper()
    # create intermediate cipher alphabet shifted with key
    CIPHER_ALBAPHET_UPPER = shift(string.ascii_uppercase, -key)
    # Translation table that map classic alphabet to cipher alphabet shifted with the key. In the
    # case of characters that are not in plain alphabet, they remain unchanged, such as spaces.
    TRANSLATION_TABLE = plain_text_upper.maketrans(string.ascii_uppercase, CIPHER_ALBAPHET_UPPER)
    # apply translation
    return plain_text_upper.translate(TRANSLATION_TABLE)


def do_decipher(cipher_text: str, key: int) -> str:
    """
    Decipher encrypted text from caesar encryption key.
    Operations are symmetric to do_cipher, thus we call it with opposed key.
    """
    return do_cipher(cipher_text, -key)


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
