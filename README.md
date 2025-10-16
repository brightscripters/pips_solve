# NYT Pips solver

## Piece
* Pair of numbers.
+ Four States
    * Swapped: Bool
    * Rotated: Bool (90deg cw)


## Placing
Linked list of nodes.
Each node represents a piece placed on the board.


## Square
A coordinate on the game board.
Origin is top left.
Positive y is downwards.


## Board
Collection of squares
Virtual two dimensional array.
Implemented as dict with tuple for key.

board[(0,0)] = newSquare(...)


## Conditions
* Set of named conditions.
* Functions


# Example
H Shape.
5 squares high.
4 squares wide.