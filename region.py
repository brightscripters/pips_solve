
import sys

class region:
    def __init__(self, topLeft = (0,0), cols = 2, rows = 5, excludedRegions = [] ):
        
        if cols == 0 or rows == 0:
            sys.exit("ERROR: Region dimension cannot be 0.")

        self.topLeft = topLeft
        self.cols = cols
        self.rows = rows
        # self.grid = [ [-1] * cols ] * rows
        self.grid = []

        # Populate grid with -1 (available)
        for n in range( 0, rows ):
            self.grid.append([-1]*cols)
        
        # Set excluded regions to None
        for excludedRegion in excludedRegions:
            for n in range( 0, excludedRegion.cols ):
                for m in range(0, excludedRegion.rows ):
                    self.grid[ m + excludedRegion.topLeft[1] ][ n + excludedRegion.topLeft[0] ] = None


    def __str__(self):
        topLeftStr = ''
        if self.topLeft != (0,0):
            topLeftStr = '@' + str( self.topLeft )

        return f"{topLeftStr} { len( self.grid[0] ) } x { len( self.grid ) } "
    

    def print(self):
        for row in self.grid:
            print(row)

hole1 = region( (1,2), 1, 1 )
hole2 = region( (1,3), 2, 2 )
reg = region(cols=5, rows=5, excludedRegions = [hole1, hole2])

print(reg)
reg.print()