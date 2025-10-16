# New square
def newSquare():
    return {''}

# Piece class
class piece:
    def __init__(self, numbers):
        self.numbers = numbers # Array [0,1]
        self.rotated = False

    def swap(self):
        firstNumber = self.numbers[0]
        self.numbers[0] = self.numbers[1]
        self.numbers[1] = firstNumber


    # Toggle rotation state
    def rotate(self):
        if self.rotated:
            self.rotated = False
        else:
            self.rotated = True
        
