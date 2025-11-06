# NYT Pips solver

## Piece
* Pair of numbers.

### Piece rotation CW
    0 No rotation
    1 90 deg CW
    2 180 deg CW
    3 270 deg CW

### Piece flipping
Piece numbers swapped.

## Placement
A placement is a vector of coordinate on the board, piece rotation, and flip.
Not specific to a particular piece.


## Square
A coordinate on the game board.
Origin is top left.
Positive y is downwards.


## Board
Collection of squares
Virtual two dimensional array.
Implemented as dict with tuple for key.

board[(0,0)] = newSquare(...)


## Condition
Restriction at a set of coordinates.

## Conditions
* Set of named conditions.
* Functions


# Example
H Shape.
5 squares high.
4 squares wide.