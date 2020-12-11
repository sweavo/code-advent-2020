import day11input

""" review: it smells bad to do so many string comparisons.  Profiling shows
    the majority of the time is spend in neighborhood, in the list comprehension
    there.  But is that because neighborhood is being called too often or because
    it is too slow?  TODO: try both options and see what happens to the profile
    """

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
    """ Abstract a 2-d array that provides a default value for out-of-bounds """
    def __init__(self, rows, default=' ', pad=1 ):
        self._maxx = len(rows[0])
        self._maxy = len(rows)
        self._pad=pad
        self._oob = default
        empty_row = default * (self._maxx + 2*pad)
        ypad = [empty_row] * pad
        xpad = default * pad
        self._rows = ypad + [ f'{xpad}{row}{xpad}' for row in rows ] + ypad

    def cells(self, xmin, ymin, xmax, ymax):
        """ a faster way to get a rectangle of values from the grid
        >>> Grid(EXAMPLE_SEATING,' ').cells(0,0,3,3)
        ['L.L', 'LLL', 'L.L']
        >>> Grid(EXAMPLE_SEATING,' ',2).cells(-2,-2,1,1)
        ['   ', '   ', '  L']
        >>> Grid(EXAMPLE_SEATING,' ',2).cells(8,8,11,11)
        ['.L ', 'LL ', '   ']
        """
        return [row[xmin+self._pad:xmax+self._pad] 
                for row in self._rows[ymin+self._pad:ymax+self._pad] ]

    def limits(self):
        return self._maxx, self._maxy

    def __repr__(self):
        """ A little extra to help testing with doctest 
        >>> Grid(['xox','o o','xox'])
        Grid(['xox',
              'o o',
              'xox'])
        """
        preamble = f'{self.__class__.__name__}(['
        indent = ' ' * len(preamble)
        return '\n'.join( [
            (preamble if y == 0 else indent)
            + repr(row)
            + (',' if y < self._maxy-1 else '])')
            for y, row in enumerate(self.cells(0,0,self._maxx,self._maxy)) ] )
            

class WaitingRoom(Grid):
    def __init__(self, rows):
        super().__init__(rows, default='.')

    def __eq__(self,other):
        """ does == work?
        >>> WaitingRoom(EXAMPLE_SEATING) == WaitingRoom(EXAMPLE_SEATING)
        True
        """
        return self._rows == other._rows
            
    def neighborhood(self,x,y):
        """
        >>> wr = WaitingRoom(EXAMPLE_SEATING)
        >>> wr.neighborhood(1,1)
        'L.LLLLL.L'
        >>> wr.neighborhood(0,0)
        '....L..LL'
        """
        return ''.join( self.cells(x-1,y-1,x+2,y+2) )

    def count(self, char):
        return sum([row.count(char) for row in self._rows])

def day11_automaton( neighborhood ):
    """ implement the cellular automaton explained in the puzzle.
    >>> day11_automaton('....L....')
    '#'
    >>> day11_automaton('LLLLLLLLL')
    '#'
    >>> day11_automaton('...L#L.L.')
    '#'
    >>> day11_automaton('.L.L#L.L.')
    '#'
    >>> day11_automaton('LLLL#LLLL')
    '#'
    >>> day11_automaton('...###.#.')
    '#'
    >>> day11_automaton('.#.###.#.')
    'L'
    >>> day11_automaton('#L#L##L#L')
    'L'
    """
    cell = neighborhood[4]
    if cell == '.':
        return '.'
    else:
        occupied_count = neighborhood.count('#')
        if cell == 'L' and occupied_count == 0:
            return '#'
        elif cell == '#' and occupied_count > 4: #count includes cell
            return 'L'
        else:
            return cell

def next_frame(frame, rule):
    """
    >>> n = next_frame(WaitingRoom(EXAMPLE_SEATING),day11_automaton)
    >>> n
    WaitingRoom(['#.##.##.##',
                 '#######.##',
                 '#.#.#..#..',
                 '####.##.##',
                 '#.##.##.##',
                 '#.#####.##',
                 '..#.#.....',
                 '##########',
                 '#.######.#',
                 '#.#####.##'])
    >>> next_frame(n,day11_automaton)
    WaitingRoom(['#.LL.L#.##',
                 '#LLLLLL.L#',
                 'L.L.L..L..',
                 '#LLL.LL.L#',
                 '#.LL.LL.LL',
                 '#.LLLL#.##',
                 '..L.L.....',
                 '#LLLLLLLL#',
                 '#.LLLLLL.L',
                 '#.#LLLL.##'])

    """
    mx,my = frame.limits()
    return WaitingRoom([
        ''.join( [rule(frame.neighborhood(x,y)) for x in range(mx)] )
        for y in range(my)])
                
def iterate_to_stable(frame, rule):
    """
    >>> frames=list(iterate_to_stable(WaitingRoom(EXAMPLE_SEATING), day11_automaton))
    >>> frames[-1].count('#')
    37
    """
    nn = next_frame(frame,rule)
    while nn != frame:
        yield nn
        frame = nn
        nn = next_frame(frame,rule)

def day11_1():
    """
    >>> day11_1()
    2299
    """
    frames = list(iterate_to_stable(WaitingRoom(day11input.SEATING), day11_automaton))
    return frames[-1].count('#')

if __name__ == "__main__":
    print(day11_1())
