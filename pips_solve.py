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
    for i in ( hor, lastX ):
        if board[i] == -1:
            if i+1 <= lastX:
                return i
            else:
                return None
        # print('i:',i)

    return None

##########################################################

# Print pieces
# for piece in pieces:
#     print(piece.numbers,'\n')

# Print summary of counts
# print("counts: ", json.dumps( countNumbers(pieces), indent=4, sort_keys=True ),'\n' )

nextAvailable = fineNextAvailable(board, 0)
print('next: ', nextAvailable)

board[0] = -2
print(board)
nextAvailable = fineNextAvailable(board, 5)
print('next: ', nextAvailable)


print("DONE")