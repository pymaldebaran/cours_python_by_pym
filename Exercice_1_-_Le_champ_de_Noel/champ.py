#!/usr/bin/env python3

from random import randrange

def main():
    NB_COLUMN = 10  # Sans les bordures (+2)
    NB_LINES = 5  # Sans les bordures (+2)
    VERTICAL_EDGE = (NB_COLUMN + 2) * '#'
    NB_TREES = 5

    LINE_WO_TREE = '#' + ' ' * (NB_COLUMN) + '#'
    line_w_trees = ['#'] + [' '] * (NB_COLUMN) + ['#']

    TREE_COORD = []
    X_COORD = []   
    Y_COORD = []

    for tree in range(NB_TREES):
        TREE_COORD.append((randrange(1, NB_COLUMN + 1),randrange(1, NB_LINES + 1)))
        X_COORD.append(TREE_COORD[tree][0])
        Y_COORD.append(TREE_COORD[tree][1])

    print(TREE_COORD,"\n")
    print(X_COORD)
    print(Y_COORD, "\n")   


    print(VERTICAL_EDGE)
    for i in range(1, NB_LINES + 1):
        if i in Y_COORD:
            for (x,y) in TREE_COORD:
                if i == y:
                    line_w_trees.remove(' ')
                    line_w_trees.insert(x,'o')
            print(''.join(line_w_trees))
            for o in line_w_trees:
                if o == 'o':
                    line_w_trees.remove('o')
                    line_w_trees.insert(x,' ')
        else:
            print(LINE_WO_TREE)
    print(VERTICAL_EDGE)   
    
if __name__ == '__main__':
    main()
