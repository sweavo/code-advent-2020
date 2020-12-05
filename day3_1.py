from day2_1 import count_letter

from day3input import DAY3_INPUT

MAP_FRAGMENT=[
    "..##.......",
    "#...#...#..",
    ".#....#..#.",
    "..#.#...#.#",
    ".#...##..#.",
    "..#.##.....",
    ".#.#.#....#",
    ".#........#",
    "#.##...#...",
    "#...##....#",
    ".#..#...#.#" ]

def whats_at( map_fragment, x, y ):
    """
        >>> whats_at( MAP_FRAGMENT, 0, 0 ) 
        '.'
        >>> whats_at( MAP_FRAGMENT, 3, 0 ) 
        '#'
        >>> whats_at( MAP_FRAGMENT, 14, 0 ) 
        '#'
        >>> whats_at( MAP_FRAGMENT, 0, 8 ) 
        '#'
        >>> whats_at( MAP_FRAGMENT, 0, 11 ) 
        """
    if y >= len(map_fragment):
        return None
    row = map_fragment[y]
    return row[ x % len(row) ]


def enumerate_slope( map_fragment, dx ,dy ):
    """
        >>> enumerate_slope( MAP_FRAGMENT, 3, 1 )
        '.#.##.####'
        """
    x = 0
    y = 0
    r = '>'
    answer = ''
    while r:
        answer += r
        x += dx
        y += dy
        r = whats_at( map_fragment, x, y )
       
    return answer[1:]

def count_slope( map_fragment, slope ):
    """
        >>> count_slope( MAP_FRAGMENT, (3,1) )
        7
        """
    return count_letter('#', enumerate_slope( map_fragment, *slope ) )

def day3_1( ):
    """
        >>> day3_1()
        242
        """
    return count_slope( DAY3_INPUT, (3,1) ) 

if __name__ == "__main__": # pragma: no cover
    day3_1()

