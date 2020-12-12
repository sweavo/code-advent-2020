""" day12_2: waypoint navigation """
import day12_1
import day12input

class Waypoint(object):
    """ Waypoint's coords are always relative to the ship, so we do not need
    a dependency on the Ferry class
    >>> w=Waypoint(lambda tup: print(f'Moved: {tup}'))
    >>> w
    Waypoint(10, 1)
    >>> w.move('F10')
    Moved: (100, 10)
    Waypoint(10, 1)
    >>> w.move('N3')
    Waypoint(10, 4)
    >>> w.move('F7')
    Moved: (70, 28)
    Waypoint(10, 4)
    >>> w.move('L90')
    Waypoint(-4, 10)
    >>> w.move('R180')
    Waypoint(4, -10)
    >>> w.move('F11')
    Moved: (44, -110)
    Waypoint(4, -10)
    """
    def __init__(elf, ferry_callback):
        elf.e = 10
        elf.n = 1
        elf._ferry_callback = ferry_callback

    def move(elf, instruction):
        operator, operand = instruction[0], int(instruction[1:])

        if operator in day12_1.ORDINALS:
            dx,dy = day12_1.ORDINALS[operator]
            elf.e += dx * operand
            elf.n += dy * operand
        
        elif operator == 'F':
            elf._ferry_callback((elf.e * operand, 
                                  elf.n * operand)) 
        
        elif operator == 'R':
            for i in range(operand // 90):
                north = -elf.e
                elf.e = elf.n
                elf.n = north

        elif operator == 'L':
            for i in range(operand // 90):
                north = elf.e
                elf.e = -elf.n
                elf.n = north

        return elf # for method chaining

    def navigate(elf,instructions):
        for instruction in instructions:
            elf.move(instruction)
        
        return elf # for method chainging

    def manhattan_distance(elf):
        return abs(elf.e) + abs(elf.n)

    def __repr__(elf):
        return f'{elf.__class__.__name__}({elf.e}, {elf.n})'

class Ferry(object):
    """ This ferry just translates by tuples """
    def __init__(elf):
        elf.e=0
        elf.n=0

    def manhattan_distance(elf):
        return abs(elf.e) + abs(elf.n)

    def translate(elf,tup):
        elf.e += tup[0]
        elf.n += tup[1]

def day12_2_solver(route):
    """
    >>> day12_2_solver(day12_1.EXAMPLE)
    286
    """
    ferry = Ferry()
    waypoint = Waypoint(ferry.translate).navigate(route)
    return ferry.manhattan_distance()

def day12_2():
    """
    >>> day12_2()
    51249
    """
    return day12_2_solver(day12input.ROUTE)

