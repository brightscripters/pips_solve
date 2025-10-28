# New square
def newSquare():
    return {''}

# Domino Piece class
class piece:
    def __init__(self, a, b ):
        self.a = a
        self.b = b

    # Rotation: 0, 1, 2, 3
    # Retruns rotated piece
    def rotate(self, rotation):

        if not rotation in range(0,4):
            print("ERROR: Rotation must be in range 0 to 3")
            exit()

        match rotation:
            case 0:
                return [[self.a, self.b],[None, None]]

            case 1:
                return [[self.a, None],[self.b, None]]

            case 2:
                return [[self.b, self.a],[None, None]]

            case 3:
                return [[self.b, None],[self.a, None]]


        
