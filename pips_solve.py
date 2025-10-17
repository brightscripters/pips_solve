print("\nPips\n")

import json
from collections import defaultdict

from game1 import pieces, groups, board



# Counts numbers appearance
def countNumbers(pieces):
    counts = defaultdict(int)
    
    for piece in pieces:
        counts[ piece.numbers[0] ] += 1
        counts[ piece.numbers[1] ] += 1

    return counts


def findNextPosition(board, hor ):
    lastX = len(board) - 1
    for i in range( hor, len(board) ):
        # print('i:',i)
        if board[i] == -1:
            if i+1 <= lastX and board[i+1] == -1:
                return i
            else:
                # print('None found')
                return None

    # print('out of elements')
    return None


def placePiece(board, position, piece):
    boardClone = board.copy()
    boardClone[position]     = piece.numbers[0]
    boardClone[position+1]   = piece.numbers[1]
    return boardClone


def fits(board, nextPosition, nextPiece):
    return True

##########################################################

# Print pieces
# for piece in pieces:
#     print(piece.numbers,'\n')

# Print summary of counts
# print("counts: ", json.dumps( countNumbers(pieces), indent=4, sort_keys=True ),'\n' )

# Record failures so we don't repeat them
# Failure captures piece, its rotation and position. 
fails = {}

# Store sequnce of board and fails
stack = []

nextPosition = findNextPosition(board, 0)
print('next: ', nextPosition)
# nextPiece = pieces.pop(0)

while nextPosition is not None and len(pieces) >= 0:
    
    # Try next piece
    nextPiece = pieces.pop(0)

    if fits(board, nextPosition, nextPiece):
        # Take snapshot
        stack.append([board,list(pieces), fails, nextPosition])
        
        board = placePiece(board, nextPosition, nextPiece )
        # print('Board:',board)
        nextPosition = findNextPosition(board, nextPosition)

        print('next: ', nextPosition)
    else:
        # Put back at end
        pieces.append(nextPiece)


# Last snapshot
stack.append([board, list(pieces), fails, nextPosition])

# Print board snapshots
for step in stack:
    print(step[0])


print("DONE")