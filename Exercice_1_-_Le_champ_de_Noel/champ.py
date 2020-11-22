#!/usr/bin/env python3

from random import randrange

def main():
    TREE = ["   ^","  ^ ^"," ( o )","( o o )","   U"] # Columns = 7 Lines = 5
    NB_TREES = 2
    
    NB_COLUMN = 20  # Min 7+2+2 = 11 (sans les bordures (+2))
    NB_LINES = 12   # Min 5+3 = 8 (sans les bordures (+2))
    
    VERTICAL_EDGE = (NB_COLUMN + 2) * '#'
    LINE_WO_TREE = '#' + ' ' * (NB_COLUMN) + '#'
    forest = [VERTICAL_EDGE] + [LINE_WO_TREE for i in range(NB_LINES)] + [VERTICAL_EDGE]
    
    TREE_COORD = [(randrange(4, NB_COLUMN + 1 - 3),randrange(5, NB_LINES + 1)) for tree in range(NB_TREES)]

    TREE_COORD = sorted(TREE_COORD, key=lambda y: y[1]) 
    X_COORD = [TREE_COORD[tree][0] for tree in range(NB_TREES)]   
    Y_COORD = [TREE_COORD[tree][1] for tree in range(NB_TREES)]    
    
    print(TREE_COORD)
    print(X_COORD)
    print(Y_COORD, "\n")
    
    for y in range(NB_LINES+2):
        forest[y] = list(forest[y].strip())
       
    for i in range(NB_TREES):  
        forest[Y_COORD[i]-4][X_COORD[i]-3:(X_COORD[i]-3+len(TREE[0]))] = TREE[0]
        forest[Y_COORD[i]-3][X_COORD[i]-3:(X_COORD[i]-3+len(TREE[1]))] = TREE[1]
        forest[Y_COORD[i]-2][X_COORD[i]-3:(X_COORD[i]-3+len(TREE[2]))] = TREE[2] 
        forest[Y_COORD[i]-1][X_COORD[i]-3:(X_COORD[i]-3+len(TREE[3]))] = TREE[3]
        forest[Y_COORD[i]-0][X_COORD[i]-3:(X_COORD[i]-3+len(TREE[4]))] = TREE[4]        
        
    for i in range(len(forest)):
        print(''.join(forest[i]))    
    print("\n") 
    
if __name__ == '__main__':
    main()
