# Game 1
# Horizontal line
# Without rotation

from pips import piece, newSquare

# Available pieces
pieces = []
pieces.append( piece([1,2]) )
pieces.append( piece([3,4]) )
pieces.append( piece([5,6]) )


# Groups
# Lists of grouped coordinates with a rule.

groups = {}


# The board
# rows, cols = 3, 3
# grid = [[0 for _ in range(cols)] for _ in range(rows)]
board = [-1] * 6

print('Board: ', board)

