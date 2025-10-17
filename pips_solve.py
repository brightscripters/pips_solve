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


def fineNextAvailable(board, hor ):
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
    boardClone[position]     = piece[0]
    boardClone[position+1]   = piece[1]
    return boardClone

##########################################################

# Print pieces
# for piece in pieces:
#     print(piece.numbers,'\n')

# Print summary of counts
# print("counts: ", json.dumps( countNumbers(pieces), indent=4, sort_keys=True ),'\n' )

# Record failures so we don't repeat them
fails = {}

# Store sequnce of board and fails
stack = []

nextAvailable = fineNextAvailable(board, 0)
print('next: ', nextAvailable)


while nextAvailable is not None:
    
    # Take snapshot
    stack.append([board,pieces, fails, nextAvailable])
    
    board = placePiece(board, nextAvailable, pieces[0].numbers )
    # print('Board:',board)
    nextAvailable = fineNextAvailable(board, nextAvailable)

    print('next: ', nextAvailable)

# Last snapshot
stack.append([board,pieces, fails, nextAvailable])

# Print board snapshots
for step in stack:
    print(step[0])


print("DONE")