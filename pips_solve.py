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
    board[position]     = piece[0]
    board[position+1]   = piece[1]

##########################################################

# Print pieces
# for piece in pieces:
#     print(piece.numbers,'\n')

# Print summary of counts
# print("counts: ", json.dumps( countNumbers(pieces), indent=4, sort_keys=True ),'\n' )

nextAvailable = fineNextAvailable(board, 0)
print('next: ', nextAvailable)

while nextAvailable is not None:
    placePiece(board, nextAvailable, (0,0))
    print('Board:',board)
    nextAvailable = fineNextAvailable(board, nextAvailable)
    print('next: ', nextAvailable)


print("DONE")