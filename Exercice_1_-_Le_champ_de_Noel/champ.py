from random import *

column = 5 #sans les bordures (+2)
line = 5 #sans les bordures (+2)



rand_column = randrange(1,column+1) 
rand_line = randrange(1,line+1)
print(rand_column)
print(rand_line)

list_sans_arbre = ['#'] + [' ']*(column) + ['#']
list_arbre = ['#'] + [' ']*(column-1) + ['#']


print((column+2)*"#")
for i in range(1,line+1):
    
    if i != rand_line :
        print ("".join(list_sans_arbre))
    else:
        
        list_arbre.insert(rand_column,'o')
        print ("".join(list_arbre))
print((column+2)*"#")
