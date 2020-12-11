import functools

import day11_1
import day11input

RAYCAST_CHECK1=day11_1.prepare_input([
    ".......#.",
    "...#.....",
    ".#.......",
    ".........",
    "..#L....#",
    "....#....",
    ".........",
    "#........",
    "...#....." ])

RAYCAST_CHECK2=day11_1.prepare_input([
    ".............",
    ".L.L.#.#.#.#.",
    "............." ])

RAYCAST_CHECK3=day11_1.prepare_input([
    ".##.##.",
    "#.#.#.#",
    "##...##",
    "...L...",
    "##...##",
    "#.#.#.#",
    ".##.##."])

RAYCAST_VECTORS=[(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]


def raycast_count( SPAN, values, index ):
    """ replacement counting function for part 2
    >>> w,v = RAYCAST_CHECK1
    >>> raycast_count( w+1, v, 53 )
    8
    >>> w,v = RAYCAST_CHECK2
    >>> raycast_count( w+1, v, 31 )
    1
    >>> w,v = RAYCAST_CHECK3
    >>> v[35]
    0
    >>> raycast_count( w+1, v, 35 )
    0
    """
    caster = functools.partial(cast_ray,SPAN,values,index)
    return sum( map (caster, RAYCAST_VECTORS) )

def cast_ray( SPAN, values, index, vector ):
    """ 
    >>> w, v = RAYCAST_CHECK2
    >>> v[29]
    0
    >>> v[30]
    False
    >>> v[31]
    0
    >>> cast_ray( w+1, v, 31, (1, 0))
    1
    >>> cast_ray( w+1, v, 31, (-1, 0))
    0
    >>> w, v = RAYCAST_CHECK3 
    >>> cast_ray( w+1, v, 35, (0, 1))
    0
    >>> cast_ray( w+1, v, 35, (1, 1))
    0
    >>> cast_ray( w+1, v, 35, (1, 0))
    0
    >>> cast_ray( w+1, v, 35, (1, -1))
    0
    >>> cast_ray( w+1, v, 35, (0, -1))
    0
    >>> cast_ray( w+1, v, 35, (-1, -1))
    0
    >>> cast_ray( w+1, v, 35, (-1, 0))
    0
    >>> cast_ray( w+1, v, 35, (-1, 1))
    0
    """
    # convert the x and y to a value to add 
    dx, dy=vector
    JUMP = SPAN*dy + dx
    MAX_INDEX = len(values)
    cursor = index+ JUMP
    while cursor >=0 and ( (cursor+1) % SPAN) and cursor < MAX_INDEX:
        if values[cursor] is not False:
            return values[cursor]
        cursor+=JUMP
    return False
       
def day11_solver( seating_plan ):
    """
    >>> day11_solver(day11_1.EXAMPLE_SEATING)
    26
    """ 
    w, v = day11_1.prepare_input(seating_plan)
    return sum(day11_1.iterate_until_stable(w, v, raycast_count, 5))

def day11_2():
    """
    >>> day11_2()
    2047
    """
    return day11_solver(day11input.SEATING)

