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


def findFreeSpace(board, square ):
    lastX = len(board) - 1
    for i in range( square[0], len(board) ):
        # print('i:',i)
        if board[i] == -1:
            if i+1 <= lastX and board[i+1] == -1:
                return (i,0,0)
            else:
                # print('None found')
                return None

    # print('out of elements')
    return None


def placePiece(board, placement, piece):
    boardClone = board.copy()
    boardClone[placement[0]]     = piece.numbers[0]
    boardClone[placement[0]+1]   = piece.numbers[1]
    return boardClone


def failed(board, freeSpace, nextPiece):
    return False


##########################################################

# Print pieces
# for piece in pieces:
#     print(piece.numbers,'\n')

# Print summary of counts
# print("counts: ", json.dumps( countNumbers(pieces), indent=4, sort_keys=True ),'\n' )

# Record failures so we don't repeat them
# Failure captures piece, and its placement. 
fails = set()

# Store sequnce of board and fails
snapshots = []

firstSquare = (0,0)

# Placement (x,y,rotation)
freeSpace = findFreeSpace(board, firstSquare )
print('next: ', freeSpace)

while freeSpace is not None and len(pieces) >= 0:
    
    # Try next piece
    nextPiece = pieces.pop(0)

    # Take snapshot
    snapshots.append([ board,list(pieces), fails ])
    
    board = placePiece( board, freeSpace, nextPiece )

    # First failure
    if failed(board, freeSpace, nextPiece):
        # Undo
        board, pieces, fails = snapshots.pop()

        # Add placement and piece to fails.
        fails.add( ( freeSpace, nextPiece ) )

        board = placePiece( board, freeSpace, nextPiece.flip() )

    # Second failure after piece flipped.
    if failed(board, freeSpace, nextPiece):
        # Undo
        board, pieces, fails = snapshots.pop()

        # Add placement and piece to fails.
        fails.add( ( freeSpace, nextPiece ) )

        # Put piece back at end of list
        pieces.append( nextPiece )

    freeSpace = findFreeSpace( board, freeSpace[0:1] )
    print( 'next: ', freeSpace )
    

# Last snapshot
snapshots.append([board, list(pieces), fails, freeSpace])

# Print board snapshots
for step in snapshots:
    print(step[0])


print("DONE")