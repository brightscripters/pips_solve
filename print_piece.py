import pips

def printPiece(piece):
    a,b = piece.nums
    print('╔' + '═══' + '╦' + '═══' + '╗')
    print('║' + ' ' + str(a) + ' ' + '║' + ' ' + str(b) + ' ' + '║')
    print('╚' + '═══' + '╩' + '═══' + '╝')


oneTwo = pips.piece(1,2)
threeFour = pips.piece(3,4)

printPiece(oneTwo)
printPiece(threeFour)