# Exercice 2 - Découvrons le chiffre de César

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

## Exercice 2.1 : Chiffrer et déchiffrer

Nous allons commencer par faire ce qu'il y a de plus simple : nous allons **chiffrer** puis **déchiffrer** un message. Pour cela nous allons utiliser une méthode extrêmement ancienne le "chiffre de César". Jules César l'utilisait pour ses correspondances... donc aux allentour du premier siècle avant JC.

Comme on code en anglais on va parler de :

- texte clair --> plain text
- texte chiffré --> cipher text
- alphabet clair --> plain alphabet
- alphabet chiffré --> cipher alphabet (souvent juste appelé "cipher")
- clé (de chiffrement) --> key

Le chiffre de César consiste simplement à décaler les lettres de l'alphabet de quelques crans vers la droite ou la gauche.

### Exemple

Par exemple, décalons les lettres de 3 rangs vers la droite (on dit qu'il a une clé de +3) :

key: +3
plain:  ABCDEFGHIJKLMNOPQRSTUVWXYZ
cipher: XYZABCDEFGHIJKLMNOPQRSTUVW

Ce qui va donner par exemple (on convertit tout en majuscule et on garde les espaces inchangés car c'est plus simple comme ça):

plain text:  Ave Caesar morituri te salutant
cipher text: XSB ZXBPXO JLOFQROF QB PXIRQXKQ

### Tes outils

Pour réaliser ça tu auras besoin de 2 fonctions qui permettent de traiter les lettre comme leurs valeur ASCII (encodage standard des caractères sous forme de nombre). Si tu te demandes pourquoi 'A' correspond au numéro 65 au lieu de 1... c'est juste qu'on a mis toutes les lettres minusculesla ponctuation et autres bizarreries avant les lettres :

```shell
>>> ord('A')
65
>>> ord('B')
66
>>> ord('C')
67
```

Et on peut faire l'opération inverse :

```shell
>>> chr(65)
'A'
>>> chr(66)
'B'
>>> chr(67)
'C'
```

### Petit piège à éviter

Je t'invite tout de même à faire attention... dans le chiffre de César l'alphabet "boucle" donc il va falloir que tu trouve un moyen pour éviter que Z se transforme en n'importe quoi par exemple :

```shell
>>> ord('Z')
90
>>> chr(90)
'Z'
>>> chr(90+3)
']'
```

## Exercice 2.2

Maintenant qu'onsait chiffer et déchiffrer, il reste la vraie partie intéressante: Décrypter !!!!

Donc tu vas essayer de retrouver un message clair à partir du message chiffré mais sans connaître la clé. Oui c'est beaucoup plus dur. Mais l'objectif ici n'est pas de tester tes connaissances en cryptographie mais de te faire progresser en programmation, je vais donc te donner la stratégie en employer pour "casser" le chiffre de César.

### Terminologie

On va une fois encore tout bien parler anglais :

- décrypter --> **crack** ou éventuellement **decrypt**

Mais tout le monde utilise **crack** donc nous aussi.

### Comment casser le chiffre de César

En fait le chiffre de César est un chiffre à substitution alphabétique (on remplace chaque lettre du message clair par une autre lettre). C'est un code très, très ancien et il a fallut très longtemps pour savoir le casser... Donc comment fait-on ? L'idée est d'utiliser la fréquence d'apparition de chaque lettre. Pour chaque langue, les différente lettre de l'alphabet ont plus ou moins de chance d'apparaitre dans un texte. Par exemple en français la lettre qui a le plus de chance d'apparaître est toujours le "e" (12.10%). Donc quelque soit la lettre que tu trouve dans le message chiffré et qui apparait le plus souvent, tu sais que c'est un "e". Idem pour la deuxième lettre la plus fréquente, le "a" (7.11%), et la troisième, le "i" (6.59%), les écart avec les autres lettres est assez énorme : [fréquence d'apparition des lettre en français](https://fr.wikipedia.org/wiki/Fr%C3%A9quence_d%27apparition_des_lettres_en_fran%C3%A7ais).

En fait vu comment fonctionne le chiffre de César dès que vous avez une lettre du message, en l'occurence le "e", vous avez gagné car vous pouvez retrouver la clé : `ord(lettre_la plus_frequente) - ord("e")`. Oui mais, me diras-tu, là on a supposé qu'on savait que le message est en français ! Si c'est une autre langue ? Hein ? Bah ça change pas grand chose : quasi toutes les langues européennes ont la même lettre la plus fréquente : le "e". Donc on ne va pas s'en occuper de cette histoire de langue.

Voilà pourquoi le chiffre de César est considéré comme un chiffre très faible : c'est simple comme tout de le casser.

Note : si le message clair est très court cette technique ne marche plus car les fréquence peuvent être localement différente. Ou alors si vous tomber sur un texte aux fréquence particulièrement atypique, comme le livre [_La Disparition_ de Georges Perec](https://fr.wikipedia.org/wiki/La_Disparition_(roman)) écrit entièrement sans la lettre "e" (je vous le conseil, comme tout Pérec c'est très très bon).

### Concrètement on fait quoi ?

On procède en deux temps :

1. On intercepte un message chiffré (et on butte le messager pour qu'il dise rien !). Je t'épargne cette étape.
2. On analyse le message intercepté pour en déduire la clé, on dit qu'on crack la clé.
3. On utilise la clé crackée pour décrypter le texte intercepté et obtenir le texte décrypté.

Comme je suis gentil j'ai donné un texte pas chiant, sans caractère accentué et qui a des fréquences relativement classiques pour du français.

### Petit piège à éviter

Quand on compte les féquences des lettres on ne compte... que les lettres ! Et on se fiche de savoir si celles-ci sont en majuscule ou minuscule.

On définit donc la fréquence d'une lettre dans un texte comme :

fréquence(lettre, texte) = nombre_d_occurence_dans le texte(lettre, texte) / nombre_total_de lettre_dans_le_texte(texte)

### Pour t'amusez

J'ai caché un petit message secret. Sauras tu en retrouver le sens ?

YQE OTQDE QZRMZFE,

V'QEBQDQ  CGQ  HAGE  MUYQDQL  XQE  BQFUFQE  OTAEQE  CGQ  VQ HAGE  MU  QZHAKQQE.  OAYYQ  HAGE  EQYNXQL  PQE  BXGE UZFQDQEEQE  BMD  XQE  FDMUZE,  QZ  OQ  YAYQZF,  VQ  HAGE QZHAUQ  QEEQZFUQXXQYQZF  PQE  OTAEQE  PQ  OQ  SQZDQ.  VQ HAGE  QZHAUQ  OAYYQ  FAGVAGDE  YQE  MRRQOFGQGEQE  BQZEQQE QF BXGE QZOADQ. X'AGDE BAXMUDQ QF YAU ZAGE MHAZE QFQ DMHUE  PQ  DQOQHAUD  FMZF  PQ  NQXXQE  XQFFDQE  PQ  HAGE  QF PQ  HAE  MZUYMGJ  PAYQEFUCGQE.  EU  HAGE  BQZEQL  CGQ  ZAGE ZQ  XQE  MHAZE  BME  XGQE,  HAGE  HAGE  FDAYBQL  ;  YMUE  EU HAGE  FDAGHQL  CGQ  BQG  PQ  HAE  PQYMZPQE  AZF  QFQ EMFUERMUFQE, AG QZ FAGF OME YAUZE CGQ P'MGFDQE RAUE, EAGHQZQL-HAGE  CG'M  ZAQX,  OQFFQ  MZZQQ,  UX  K  M  GZ ZAYNDQ  FQDDUNXQ  PQ  SQZE  BMGHDQE  QF  MRRMYQE  PMZE  XQ YAZPQ QZFUQD.

V'MU  PG  (QF  YAZ  RDQDQ  HQDF  MGEEU)  DMEEQYNXQD  PQ  XM ZAGDDUFGDQ  QF  PQE  HQFQYQZFE,  PQE  VAGQFE  MGEEU,  BAGD XQE QZRMZFE PAZF XQE BQDQE, XQE YQDQE QF XQE MYUE ZQ BQGHQZF DUQZ XQGD ARRDUD, BMDRAUE BME YQYQ GZ DQBME. VQ  EMUE  CGQ  HAE  BMDQZFE  QF  HAE  MYUE  ZQ  HAZF AGNXUQDAZF BME.

QZ EAYYQ, YQE OTQDUE, V'QEBQDQ CGQ HAGE EQDQL TQGDQGJ OQ ZAQX, CGQ HAGE ZQ HAGE PUEBGFQDQL BME QF CGQ HAGE HAGE  MYGEQDQL  NUQZ  FAGE  QZEQYNXQ  MHQO  HAFDQ  FDMUZ. Z'AGNXUQL  BME  XQ  HUQGJ  BQDQ  ZAQX  XADECGQ  HAGE UXXGYUZQDQL HAFDQ MDNDQ.

HAFDQ MRRQOFGQGJ BQDQ ZAQX





