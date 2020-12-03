#!/usr/bin/env python3
"""
Xmas field of trees.

A short program that generates a field with a random numbers of pretty trees, just like this one:
   ^
  ^ ^
 (o  )
(o  o )
   U

The field is delimited with the symbol `#`.
The program handles perspective, showing trees "at the bottom" in front of the other trees.
"""

import math
import random

# field constants
# minimum WIDTH and HEIGHT of 12 is adviced
WIDTH = 20
HEIGHT = 20
X_LIMITS = (0, WIDTH - 1)
Y_LIMITS = (0, HEIGHT - 1)
PROTECTION_SPAWN_LEFT = 4
PROTECTION_SPAWN_RIGHT = 4
PROTECTION_SPAWN_TOP = 1
PROTECTION_SPAWN_BOTTOM = 5
PLANTABLE_REGION_LIMITS_HORIZONTAL = (PROTECTION_SPAWN_LEFT, WIDTH - PROTECTION_SPAWN_RIGHT)
PLANTABLE_REGION_LIMTIS_VERTICAL = (PROTECTION_SPAWN_BOTTOM, HEIGHT - PROTECTION_SPAWN_TOP)
FIELD_SURFACE = WIDTH * HEIGHT

# tree constants
BORDER_CHAR = "#"
EMPTY_CHAR = " "
TREE_DESIGN = ["^", "^ ^", "(o  )", "(o  o )", "U"]
TREE_HEIGHT = len(TREE_DESIGN)
TREE_WIDTH = max(len(line) for line in TREE_DESIGN)
TREE_SURFACE = TREE_HEIGHT * TREE_WIDTH

# The maximum number of trees on the field depends on the surface of the field over the surface of
# a tree. An additional factor is provided to customize the occupation rate. If the latter is set
# to 1, then if you can place as many trees as there is field surfaces, i.e. if tree and field
# have same surface then only one tree can fit, if the field surface is twice the tree surface
# then two trees can fit.
# You can tweak this maximum number with the occupation rate, e.g. by setting it to 0.5 you only
# allow half the surface to be covered.
# However, they will be planted randomly, so even with an occupation rate lower than 1, trees
# might overlap. Nevertheless it helps limiting the number of trees, that we allow to plant.
MINIMUM_TREES = 1
TREE_OCCUPATION_RATE = 0.9
MAX_TREE_FOR_FIELD = math.floor(TREE_OCCUPATION_RATE * FIELD_SURFACE / TREE_SURFACE)


def main():
    # create field with borders
    field = [
        [BORDER_CHAR if (X in X_LIMITS or Y in Y_LIMITS) else EMPTY_CHAR for X in range(WIDTH)]
        for Y in range(HEIGHT)
    ]

    # Empiric max number of trees for the sake of visibility.
    # My goal was to have a dynamic approach for having "enough" trees to demonstrate perspective
    # but also to have "enough" probability to see a clean field with few trees.
    # Thus, both WIDTH and HEIGHT sizes contribute to the maximum number of trees, multiplied by
    # a coefficient TREE_OCCURRENCE_FACTOR to reduce the spawn occurrence of trees.
    NUMBER_TREES = random.randint(MINIMUM_TREES, MAX_TREE_FOR_FIELD)

    # get number_trees random positions in the field (excluded the border protection area)
    # list of y positions are sorted to handle perspective by planting them from top to bottom
    TREE_POSITIONS_X = random.sample(range(*PLANTABLE_REGION_LIMITS_HORIZONTAL), NUMBER_TREES)
    TREE_POSITIONS_Y = sorted(random.sample(range(*PLANTABLE_REGION_LIMTIS_VERTICAL), NUMBER_TREES))

    # plant trees from top to bottom
    for POSITION_X, POSITION_Y in zip(TREE_POSITIONS_X, TREE_POSITIONS_Y):
        # plant each tree from truc to crown
        for INDEX_LINE, TREE_LINE in enumerate(TREE_DESIGN[::-1]):
            HALF_WIDTH_TREE = int(len(TREE_LINE) / 2)
            # replace field symbols at current field line from -half_width_tree to
            #  half_width_tree + 1 around the x position of the trunk
            field[POSITION_Y - INDEX_LINE][
                POSITION_X - HALF_WIDTH_TREE : POSITION_X + HALF_WIDTH_TREE + 1
            ] = TREE_LINE

    # show the world your Xmas tree field
    for LINE in field:
        print("".join(LINE))


if __name__ == "__main__":
    main()
