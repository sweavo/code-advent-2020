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
    >>> w.move('R90')
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
            north = -elf.e
            elf.e = elf.n
            elf. n = north
            
        elif operator == 'L':
            north = elf.e
            elf.e = -elf.n
            elf. n = north
        
        return elf # for method chaining

    def navigate(elf,instructions):
        for instruction in instructions:
            elf.move(instruction)
        
        return elf # for method chainging

    def manhattan_distance(elf):
        return abs(elf.e) + abs(elf.n)

    def __repr__(elf):
        return f'{elf.__class__.__name__}({elf.e}, {elf.n})'

