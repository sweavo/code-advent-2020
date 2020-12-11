EXAMPLE_SEATING=[
    "L.LL.LL.LL",
    "LLLLLLL.LL",
    "L.L.L..L..",
    "LLLL.LL.LL",
    "L.LL.LL.LL",
    "L.LLLLL.LL",
    "..L.L.....",
    "LLLLLLLLLL",
    "L.LLLLLL.L",
    "L.LLLLL.LL" ]

class Grid(object):
    def __init__(self, rows, out_of_bounds_char=' ' ):
        self._rows = rows
        self._maxx = len(rows[0])
        self._maxy = len(rows)
        self._oob = out_of_bounds_char

    def cell(self, x, y):
        """
        >>> wr = Grid(EXAMPLE_SEATING,'X')
        >>> wr.cell(0,0)
        'L'
        >>> wr.cell(-1,0)
        'X'
        """
        if x < 0 or x >= self._maxx or y < 0 or y > self._maxy:
            return self._oob
        else:
            return self._rows[y][x]

class WaitingRoom(Grid):
    def __init__(self, rows):
        super().__init__(rows, out_of_bounds_char='.')

    def neighborhood(self,x,y):
        """
        >>> wr = WaitingRoom(EXAMPLE_SEATING)
        >>> wr.neighborhood(1,1)
        'L.LLLLL.L'
        >>> wr.neighborhood(0,0)
        '....L..LL'
        """
        return ''.join( [ self.cell(x+dx,y+dy) for dy in range(-1,2) for dx in range(-1,2) ] )

