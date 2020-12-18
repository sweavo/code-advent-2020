""" Conway cubes.

Going to keep a list of active cells, and maintain the cuboid of interest, scanning all coords within 
that range.

"""
import day17input

DEMO=[
    '.#.',
    '..#',
    '###' ]

def lines_to_field(strings):
    """
    >>> list(lines_to_field(DEMO))
    [(1, 0, 0), (2, 1, 0), (0, 2, 0), (1, 2, 0), (2, 2, 0)]
    """
    for y, row in enumerate(strings):
        for x, char in enumerate(row):
            if char == '#':
                yield (x, y, 0)

def print_map(field):
    """
    >>> print_map([(1, 0, 0), (2, 1, 0), (0, 2, 0), (1, 2, 0), (2, 2, 0)])
    z=0
    .#.
    ..#
    ###

    """
    minx, maxx, miny, maxy, minz, maxz = get_bounds(field)
    
    for z in range(minz, maxz+1): 
        print(f'z={z}')  
        for y in range(miny, maxy+1): 
            row=''
            for x in range(minx, maxx+1): 
                if (x,y,z) in field:
                    row += '#'
                else:
                    row += '.'
            print(row)
    
def count_neighborhood(field, x, y, z):
    total=0
    for dz in range(-1,2):
        for dy in range(-1,2):
            for dx in range(-1,2):
                if (x+dx,y+dy,z+dz) in field:
                    total+=1
    return total

def decide_cell(field, x, y, z):
    neighborhood = count_neighborhood(field, x, y, z)
    if (x,y,z) in field:
        if neighborhood in [3, 4]:
            return True
    else:
        if neighborhood == 3:
            return True 

    return False 
      
def get_bounds(points):
    minx, miny, minz = points[0]
    maxx, maxy, maxz = points[0]
    for x,y,z in points:
        if x<minx: minx=x
        if x>maxx: maxx=x
        if y<miny: miny=y
        if y>maxy: maxy=y
        if z<minz: minz=z
        if z>maxz: maxz=z
    return minx, maxx, miny, maxy, minz, maxz       
     
def generate_next_field( field ):
    """
    >>> f=generate_next_field(list(lines_to_field(DEMO)))
    >>> print_map(f)
    z=-1
    #..
    ..#
    .#.
    z=0
    #.#
    .##
    .#.
    z=1
    #..
    ..#
    .#.
    >>> f=generate_next_field(f)
    >>> print_map(f)
    z=-2
    .....
    .....
    ..#..
    .....
    .....
    z=-1
    ..#..
    .#..#
    ....#
    .#...
    .....
    z=0
    ##...
    ##...
    #....
    ....#
    .###.
    z=1
    ..#..
    .#..#
    ....#
    .#...
    .....
    z=2
    .....
    .....
    ..#..
    .....
    .....
    """

    minx, maxx, miny, maxy, minz, maxz = get_bounds(field)
    next_frame = [] 
    for z in range(minz-1, maxz+2): 
        for y in range(miny-1, maxy+2): 
            for x in range(minx-1, maxx+2): 
                if decide_cell(field, x,y,z):
                    next_frame.append((x,y,z))
    return next_frame

def day17_1_solver(lines, iterations):
    """
    >>> day17_1_solver(DEMO, 6)
    112
    """
    field = list(lines_to_field(lines))
    for iteration in range(iterations):
        field = list(generate_next_field(field))
    return len(field)

def day17_1():
    """
    >>> day17_1()
    336
    """
    return day17_1_solver(day17input.LINES,6)

