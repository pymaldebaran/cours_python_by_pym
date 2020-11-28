#! /usr/bin/env python3
"""
# Exercice 2.1 - Découvrons le chiffre de César

Nous allons aujourd'hui nous lancer écrire des message secret !

## Vocabulaire

Commençons par un peu de vocabulaire:

- **Cryptologie** : a cryptologie, étymologiquement la science du secret, ne peut être vraiment considérée comme une science que depuis peu de temps. Cette science englobe la cryptographie – l’écriture secrète –, la cryptanalyse – l’analyse et l’attaque de cette dernière –, et la stéganographie – l’art de la dissimulation.
- **Cryptographie** : La cryptographie est une des disciplines de la cryptologie s’attachant à protéger des messages (assurant confidentialité, authenticité et intégrité) en s’aidant souvent de secrets ou clés.
- **Chiffrement** : Le chiffrement est un procédé de cryptographie grâce auquel on souhaite rendre la compréhension d’un document impossible à toute personne qui n’a pas la clé de (dé)chiffrement. Ce principe est généralement lié au principe d’accès conditionnel.
- **Chiffrer** : L’action de procéder à un chiffrement.
- **Déchiffrer** : En informatique et en télécommunications, déchiffrer consiste à retrouver le texte original (aussi appelé clair) d’un message chiffré dont on possède la clé de (dé)chiffrement.
- **Décrypter** : Décrypter consiste à retrouver le texte original à partir d’un message chiffré sans posséder la clé de (dé)chiffrement. Décrypter ne peut accepter d’antonyme : il est en effet impossible de créer un message chiffré sans posséder de clé de chiffrement.

Attention il y a quelques mots qu'on entend souvent mais qui sont faux :

- **Crypter / Cryptage** : Le terme « cryptage » et ses dérivés viennent du grec ancien κρυπτός, kruptos, « caché, secret ». Cependant, le Référentiel Général de Sécurité de l’ANSSI qualifie d’incorrect « cryptage ». En effet, la terminologie de cryptage reviendrait à chiffrer un fichier sans en connaître la clé et donc sans pouvoir le déchiffrer ensuite. Le terme n’est par ailleurs pas reconnu par le dictionnaire de l’Académie française.
- **Encrypter / Déencrypter** : Le terme « encrypter » et ses dérivés sont des anglicismes. Donc, nan, on ne les utilise pas non plus.
- **Chiffrage** : Celui-là, c’est le pompon, la cerise sur le gâteau. Le chiffrage, c’est évaluer le coût de quelque chose. ABSOLUMENT RIEN à voir avec le chiffrement. Et pourtant, parfois, on le voit.
- **Coder / Encoder / Décoder** : Coder / Encoder signifie “Constituer (un message, un énoncé) selon les règles d’un système d’expression − langue naturelle ou artificielle, sous une forme accessible à un destinataire.” En informatique il s’agit d’une façon d’écrire les mêmes données, mais de manière différente (ex. en base64, en hexadécimal, avec des codes correcteurs d’erreurs etc…). Ce procédé est facilement inversible (il n’y a aucune notion de clé dans ces opérations), il n’y a aucune vocation à assurer la confidentialité, ce n’est donc pas du chiffrement.

## Explications

Nous allons commencer par faire ce qu'il y a de plus simple : nous allons **chiffrer** puis **déchiffrer** un message. Pour cela nous allons utiliser une méthode extrêmement ancienne le "chiffre de César". Jules César l'utilisait pour ses correspondances... donc aux allentour du premier siècle avant JC.

Comme on code en anglais on va parler de :

- texte clair --> plain text
- texte chiffré --> cipher text
- alphabet clair --> plain alphabet
- alphabet chiffré --> cipher alphabet (souvent juste appelé "cipher")
- clé (de chiffrement) --> key

Le chiffre de César consiste simplement à décaler les lettres de l'alphabet de quelques crans vers la droite ou la gauche.

## Exemple

Par exemple, décalons les lettres de 3 rangs vers la droite (on dit qu'il a une clé de +3) :

key: +3
plain:  ABCDEFGHIJKLMNOPQRSTUVWXYZ
cipher: XYZABCDEFGHIJKLMNOPQRSTUVW

Ce qui va donner par exemple (on convertit tout en majuscule et on garde les espaces inchangés car c'est plus simple comme ça):

plain text:  Ave Caesar morituri te salutant
cipher text: XSB ZXBPXO JLOFQROF QB PXIRQXKQ

## Tes outils

Pour réaliser ça tu auras besoin de 2 fonctions qui permettent de traiter les lettre comme leurs valeur ASCII (encodage standard des caractères sous forme de nombre). Si tu te demandes pourquoi 'A' correspond au numéro 65 au lieu de 1... c'est juste qu'on a mis toutes les lettres minusculesla ponctuation et autres bizarreries avant les lettres :

>>> ord('A')
65
>>> ord('B')
66
>>> ord('C')
67

Et on peut faire l'opération inverse :

>>> chr(65)
'A'
>>> chr(66)
'B'
>>> chr(67)
'C'

## Petit piège à éviter

Je t'invite tout de même à faire attention... dans le chiffre de César l'alphabet "boucle" donc il va falloir que tu trouve un moyen pour éviter que Z se transforme en n'importe quoi par exemple :

>>> ord('Z')
90
>>> chr(90)
'Z'
>>> chr(90+3)
']'
"""

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


def main():
    PLAIN_TEXT = "Ave Caesar morituri te salutant"
    KEY = 3

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


if __name__ == "__main__":
    main()
