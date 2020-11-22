#!/usr/bin/env python3

from random import randrange

def main():
    # Columns = 7 Lines = 5
    TREE = [
        "   ^",
        "  ^ ^",
        " ( o )",
        "( o o )",
        "   U"
    ]
    NB_TREES = 6

    NB_COLUMN = 60  # Min 7+2+2 = 11 (sans les bordures (+2))
    NB_LINES = 40   # Min 5+3 = 8 (sans les bordures (+2))

    VERTICAL_EDGE = (NB_COLUMN + 2) * '#'
    LINE_WO_TREE = '#' + ' ' * (NB_COLUMN) + '#'

    TREE_COORD = [(randrange(4, NB_COLUMN + 1 - 3),randrange(5, NB_LINES + 1)) for tree in range(NB_TREES)]

    TREE_COORD = sorted(TREE_COORD, key=lambda y: y[1])
    X_COORD = [TREE_COORD[tree][0] for tree in range(NB_TREES)]
    Y_COORD = [TREE_COORD[tree][1] for tree in range(NB_TREES)]

    print(TREE_COORD)
    print(X_COORD)
    print(Y_COORD, "\n")

    # J'ai descendu tout ce qui concernait la forest ici... c'est plus clair
    forest = [VERTICAL_EDGE] + [LINE_WO_TREE for i in range(NB_LINES)] + [VERTICAL_EDGE]
    for y in range(NB_LINES+2):
        forest[y] = list(forest[y].strip())

    # La nouvelle double boucle
    for i in range(NB_TREES):
        TREE_HEIGHT = len(TREE)
        X_OFFSET = 3
        for tree_line in range(TREE_HEIGHT):
            Y = Y_COORD[i] - (TREE_HEIGHT - tree_line - 1)
            X_START = X_COORD[i] - X_OFFSET
            X_END = X_COORD[i] - X_OFFSET + len(TREE[tree_line])

            forest[Y][X_START:X_END] = TREE[tree_line]

    for i in range(len(forest)):
        print(''.join(forest[i]))
    print("\n")

if __name__ == '__main__':
    main()
