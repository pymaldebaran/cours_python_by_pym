from random import randrange

COLUMN = 10  # Sans les bordures (+2)
LINE = 5  # Sans les bordures (+2)

RAND_COLUMN = randrange(1, COLUMN+1) 
RAND_LINE = randrange(1, LINE+1)
BORDURE_VERTICALE = (COLUMN + 2) * '#'

print(RAND_COLUMN)
print(RAND_LINE)

ligne_sans_arbre = '#' + ' ' * (COLUMN) + '#'
ligne_avec_arbres = '#' + ' ' * (COLUMN-1) + '#'

print(BORDURE_VERTICALE)
for i in range(1, LINE + 1):
    
    if i == RAND_LINE :             
        print (ligne_avec_arbres[:RAND_COLUMN] 
               + 'o' + ligne_avec_arbres[RAND_COLUMN:])
    else:
        print(ligne_sans_arbre)
print(BORDURE_VERTICALE)
