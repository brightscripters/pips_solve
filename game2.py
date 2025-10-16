# Game 2
# H shape

# Available pieces
pieces = []
pieces.append( piece([3,0]) )
pieces.append( piece([4,0]) )
pieces.append( piece([3,5]) )
pieces.append( piece([0,2]) )
pieces.append( piece([1,1]) )
pieces.append( piece([2,2]) )


# Groups
# Lists of grouped coordinates with a rule.

groups = {}


# The board
board = {}
board[(1,1)] = newSquare()
board[(1,2)] = newSquare()
board[(1,3)] = newSquare()
board[(1,4)] = newSquare()
board[(1,5)] = newSquare()

board[(2,3)] = newSquare()
board[(3,3)] = newSquare()

board[(4,1)] = newSquare()
board[(4,2)] = newSquare()
board[(4,3)] = newSquare()
board[(4,4)] = newSquare()
board[(4,5)] = newSquare()

