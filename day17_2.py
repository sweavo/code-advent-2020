""" Conway hyper cubes.
"""
import day17input

DEMO=[
    '.#.',
    '..#',
    '###' ]

def lines_to_field(strings):
    """
    >>> list(lines_to_field(DEMO))
    [(1, 0, 0, 0), (2, 1, 0, 0), (0, 2, 0, 0), (1, 2, 0, 0), (2, 2, 0, 0)]
    """
    for y, row in enumerate(strings):
        for x, char in enumerate(row):
            if char == '#':
                yield (x, y, 0, 0)

def print_map(field):
    """
    >>> print_map([(1, 0, 0, 0), (2, 1, 0, 0), (0, 2, 0, 0), (1, 2, 0, 0), (2, 2, 0, 0)])
    z=0, w=0
    .#.
    ..#
    ###

    """
    minx, maxx, miny, maxy, minz, maxz, minw, maxw = get_bounds(field)
   
    for w in range(minw, maxw+1): 
        for z in range(minz, maxz+1): 
            print(f'z={z}, w={w}')  
            for y in range(miny, maxy+1): 
                row=''
                for x in range(minx, maxx+1): 
                    if (x,y,z,w) in field:
                        row += '#'
                    else:
                        row += '.'
                print(row)
    
def count_neighborhood(field, x, y, z, w):
    total=0
    for dw in range(-1,2):
        for dz in range(-1,2):
            for dy in range(-1,2):
                for dx in range(-1,2):
                    if (x+dx, y+dy, z+dz, w+dw) in field:
                        total+=1
    return total

def decide_cell(field, x, y, z, w):
    neighborhood = count_neighborhood(field, x, y, z, w)
    if (x,y,z, w) in field:
        if neighborhood in [3, 4]:
            return True
    else:
        if neighborhood == 3:
            return True 

    return False 
      
def get_bounds(points):
    minx, miny, minz, minw = points[0]
    maxx, maxy, maxz, maxw = points[0]
    for x, y, z, w in points:
        if x<minx: minx=x
        if x>maxx: maxx=x
        if y<miny: miny=y
        if y>maxy: maxy=y
        if z<minz: minz=z
        if z>maxz: maxz=z
        if w<minw: minw=w
        if w>maxw: maxw=w
    return minx, maxx, miny, maxy, minz, maxz, minw, maxw
     
def generate_next_field( field, bounds):
    """
    >>> f=list(lines_to_field(DEMO))
    >>> b=get_bounds(f)
    >>> f,b=generate_next_field(f,b)
    >>> print_map(f)
    z=-1, w=-1
    #..
    ..#
    .#.
    z=0, w=-1
    #..
    ..#
    .#.
    z=1, w=-1
    #..
    ..#
    .#.
    z=-1, w=0
    #..
    ..#
    .#.
    z=0, w=0
    #.#
    .##
    .#.
    z=1, w=0
    #..
    ..#
    .#.
    z=-1, w=1
    #..
    ..#
    .#.
    z=0, w=1
    #..
    ..#
    .#.
    z=1, w=1
    #..
    ..#
    .#.
    """

    minx, maxx, miny, maxy, minz, maxz, minw, maxw = bounds
    rminx, rmaxx, rminy, rmaxy, rminz, rmaxz, rminw, rmaxw = (maxx, minx, maxy, miny, maxz, minz, maxw, minw) #note: assigned max to min etc, so that bounds are definitely derived afresh.
    next_frame = [] 
    for w in range(minw-1, maxw+2): 
        for z in range(minz-1, maxz+2): 
            for y in range(miny-1, maxy+2): 
                for x in range(minx-1, maxx+2): 
                    if decide_cell(field, x, y, z, w):
                        if x<rminx: rminx=x
                        if x>rmaxx: rmaxx=x
                        if y<rminy: rminy=y
                        if y>rmaxy: rmaxy=y
                        if z<rminz: rminz=z
                        if z>rmaxz: rmaxz=z
                        if w<rminw: rminw=w
                        if w>rmaxw: rmaxw=w
                        next_frame.append((x, y, z, w))
    return next_frame, (rminx, rmaxx, rminy, rmaxy, rminz, rmaxz, rminw, rmaxw)

def day17_2_solver(lines, iterations):
    """
    #>> day17_2_solver(DEMO, 6)
    848
    """
    field = list(lines_to_field(lines))
    bounds = get_bounds(field)
    for iteration in range(iterations):
        field, bounds = generate_next_field(field, bounds)
    return len(field)

def day17_2():
    """
    >>> day17_2()
    336
    """
    return day17_2_solver(day17input.LINES,6)

