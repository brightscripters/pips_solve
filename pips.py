import copy

# New square
def newSquare():
    return {''}

# Domino Piece class
class piece:
    def __init__(self, a, b, bOffsets = [1,0] ):
        self.nums = [a,b]
        self.bOffsets = bOffsets # Rotation: b points right, down, left, up
        self.reversed = False

    def getRotOffsets(self):
        return self.bOffsets

    # swapps self. a <-> b
    def reverse(self):
        clone = copy.deepcopy(self)
        clone.nums = [ clone.nums[1], clone.nums[0] ]
        clone.reversed = True
        return clone

    # Rotation: 0, 1, 2, 3
    # Retruns rotated piece
    def rotate(self, rotation):

        if not rotation in range(0,4):
            print("ERROR: Rotation must be in range 0 to 3")
            exit()
        
        clone = copy.deepcopy(self)

        match rotation:
            case 0: # defalt. No rotation. Pointing right.
                pass

            case 1: # down
                clone.bOffsets = [0,1]

            case 2: # left
                clone.bOffsets = [-1,0]

            case 3: # up
                clone.bOffsets = [0,-1]

        return clone

# find available piece rotations at coordinate
# returns a list of rotations
def rotationsHere(coordinate, board = [[-1,-1]]):
    x,y = coordinate
    if x < 0 or y < 0:
        breakpoint()

    rotations = []

    if isSquareAvailable(x+1, y, board):
        rotations.append(0)

    if isSquareAvailable(x, y+1, board):
        rotations.append(1)

    if isSquareAvailable(x-1, y, board):
        rotations.append(2)

    if isSquareAvailable(x, y-1, board):
        rotations.append(3)

    return rotations


def isSquareAvailable(x,y,board):
    
    # x out or range
    if x >= len(board[0]) or x < 0:
        return False

    # y out or range
    if y >= len(board) or y < 0:
        return False

    if board[y][x] == -1:
        return True

    return False

    