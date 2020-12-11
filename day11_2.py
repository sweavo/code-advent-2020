import day11input

""" After a very slow result last time, this time I will be using 
    a small numerical type to represent the grid. 0 is empty chair,
    1 is occupied chair and False is floor.  False is chosen because 
    it can be `sum()`med along with integers, but can also be detected
    by `is False`.
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

EXPECT1=[
    "#.##.##.##",
    "#######.##",
    "#.#.#..#..",
    "####.##.##",
    "#.##.##.##",
    "#.#####.##",
    "..#.#.....",
    "##########",
    "#.######.#",
    "#.#####.##" ]

EXPECT2=[
    "#.LL.L#.##",
    "#LLLLLL.L#",
    "L.L.L..L..",
    "#LLL.LL.L#",
    "#.LL.LL.LL",
    "#.LLLL#.##",
    "..L.L.....",
    "#LLLLLLLL#",
    "#.LLLLLL.L",
    "#.#LLLL.##" ]

RAYCAST_CHECK1=[
    ".......#.",
    "...#.....",
    ".#.......",
    ".........",
    "..#L....#",
    "....#....",
    ".........",
    "#........",
    "...#....." ]

RAYCAST_CHECK2=[
    ".............",
    ".L.L.#.#.#.#.",
    "............." ]

RAYCAST_CHECK3=[
    ".##.##.",
    "#.#.#.#",
    "##...##",
    "...L...",
    "##...##",
    "#.#.#.#",
    ".##.##."]

DECODE = {
    '.': False,
    'L': 0,
    '#': 1 }

ENCODE = {
    'False': '.',
    '0': 'L',
    '1': '#' }

def prepare_input(seating_plan):
    """ convert sequence of sequence of character to sequence of int. 

    Only needs doing  once per seating plan.

    Since False is completely inert in this puzzle, it is used as padding,
    an entire row's worth at the start and one False between each row. This
    means that any read out-of-bounds at the left or top returns False.
    Python takes care of out-of-bounds in the positive direction by truncating
    the result.
    
    This means that for any valid cell, it's also valid to read any
    cell from above left of it to below right of it.  As we flatten the 
    "2-d array" into 1 dimension, we return the width dimension to allow 
    the caller to subsequently navigate by row as well as by column.
    >>> tup=prepare_input( ['L.L','.#.'])
    >>> tup[0]
    3
    >>> list(tup[1])
    [False, False, False, False, 0, False, 0, False, False, 1, False]
     """
    height = len(seating_plan)
    width = len(seating_plan[0]) 
    concat='.'.join([ '.' * width  ] + seating_plan )
    return width, list(map( DECODE.get, concat ))

def prepare_output(width, values):
    """ Render a seating plan back to list-of-strings, removing padding.
    >>> list(prepare_output( 3, [False, False, False, False, 0, False, 0, False, False, 1, False] ))
    ['L.L', '.#.']
    >>> w,v = prepare_input(EXAMPLE_SEATING)
    >>> list(prepare_output(w,v))
    ['L.LL.LL.LL', 'LLLLLLL.LL', 'L.L.L..L..', 'LLLL.LL.LL', 'L.LL.LL.LL', 'L.LLLLL.LL', '..L.L.....', 'LLLLLLLLLL', 'L.LLLLLL.L', 'L.LLLLL.LL']
    """
    values =list(values)
    rows = len(values)//(width+1)
    for y in range(rows):
        yield ''.join(map(lambda x: ENCODE[str(x)],
                            values[ (y+1) * (width+1): (y+2) * (width+1)-1 ])) 
   
def day11_1_fn(SPAN, values, index):
    return sum( values[index-SPAN-1:index-SPAN+2]
                + values[index-1:index+2]
                + values[index+SPAN-1:index+SPAN+2] ) 


def apply_rules( width, values, count_fn ):
    """ given a prepared plan, the rules are very cheap to apply.

    Especially if you forego structured programming and separation of 
    concerns.  Here I mix calculating the whereabouts of the values, 
    summing them, and applying the "business rules" of flipping on or off 
    switches.

    I have to write a whole new list because I don't want to reead my 
    just-written value as part of the decision for the value below me or 
    to the right. `append` doesn't seem to be costing me too much right 
    now.
    >>> input_list = [False, False, False, False, 0]
    >>> apply_rules(3, input_list, day11_1_fn)
    (True, [False, False, False, False, 1])
    >>> input_list
    [False, False, False, False, 0]
    >>> w, v = prepare_input(EXAMPLE_SEATING)
    >>> _, expect1 = prepare_input(EXPECT1)
    >>> _, expect2 = prepare_input(EXPECT2)
    >>> _, out1 = apply_rules( w, v, day11_1_fn )
    >>> out1 == expect1
    True
    >>> _, out2 = apply_rules( w, out1, day11_1_fn )
    >>> out2 == expect1
    False
    >>> out2 == expect2
    True
    """
    SPAN=width+1
    changed=False
    result=values[:SPAN] # start with the top padding, untouched

    for index in range(SPAN,len(values)): 
        # walk through linearly, including the "right padding".
        value = values[index]
        if value is False:
            result.append(False)
        else:
            count = count_fn(SPAN, values, index )
            if value == 0 and count == 0:
                result.append(1)
                changed=True
            elif value == 1 and count > 4: # count includes this seat
                result.append(0)
                changed=True
            else:
                result.append(value)

    return (changed, result)

def iterate_until_stable( width, values ):
    """
    >>> w, v = prepare_input(EXAMPLE_SEATING)
    >>> v = iterate_until_stable( w, v )
    >>> sum(v) 
    37
    """ 
    changed=True # just to be able to enter the loop
    while changed:
        changed, values = apply_rules( width, values, day11_1_fn )
    return values
    
def day11_1():
    """
    >>> day11_1()
    2299
    """
    w, v = prepare_input(day11input.SEATING)
    return sum(iterate_until_stable(w, v))

