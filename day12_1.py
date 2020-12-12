""" day12_1: ferry navigation

To me, this is the one _definitely defensible_ use of OO. An object that 
represents a domain object.

>>> f=Ferry()
>>> f.move('F10')
Ferry(10, 0, E)
>>> f.move('N3')
Ferry(10, 3, E)
>>> f.move('F7')
Ferry(17, 3, E)
>>> f.move('R90').move('L90')
Ferry(17, 3, E)
>>> f=Ferry().sail(EXAMPLE)
>>> f.manhattan_distance()
25
"""
import day12input

EXAMPLE=[
    "F10",
    "N3",
    "F7",
    "R90",
    "F11" ]

ORDINALS={
    'E': (1, 0), 
    'S': (0, -1), 
    'W': (-1, 0), 
    'N': (0, 1)}

HEADINGS='ESWN'

class Ferry(object):
    
    def __init__(elf):
        elf.e = 0
        elf.n = 0
        elf.heading = 0 #east

    def move(elf, instruction):
        operator, operand = instruction[0], int(instruction[1:])

        if operator in ORDINALS:
            dx,dy = ORDINALS[operator]
            elf.e += dx * operand
            elf.n += dy * operand
        
        elif operator == 'F':
            dx,dy = ORDINALS[HEADINGS[elf.heading]]
            elf.e += dx * operand
            elf.n += dy * operand
        
        else: # must be rotating
            multiplier = 1 if operator == 'R' else -1
            steps = operand // 90
            elf.heading = (elf.heading + multiplier * steps) % len(HEADINGS)
        
        return elf # for method chaining

    def sail(elf,instructions):
        for instruction in instructions:
            elf.move(instruction)
        
        return elf # for method chainging

    def manhattan_distance(elf):
        return abs(elf.e) + abs(elf.n)

    def __repr__(elf):
        return f'{elf.__class__.__name__}({elf.e}, {elf.n}, {HEADINGS[elf.heading]})'

def day12_1():
    """
    >>> day12_1()
    757
    """
    return Ferry().sail(day12input.ROUTE).manhattan_distance()


