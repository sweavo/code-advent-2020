EXAMPLE_DOCKING_PROGRAM = [
    "mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
    "mem[8] = 11",
    "mem[7] = 101",
    "mem[8] = 0" ]

def mask_decode(tristatestring):
    """ Translate a tristate mask into two masks: one to be _or_ed and one to 
    be _and_ed
    >>> mask_decode("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    (0, 68719476735)
    >>> mask_decode("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX0")
    (0, 68719476734)
    >>> mask_decode("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX1")
    (1, 68719476735)
    >>> mask_decode("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX01")
    (1, 68719476733)
    >>> mask_decode("1XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    (34359738368, 68719476735)
    >>> mask_decode("1XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX0")
    (34359738368, 68719476734)
    """
    or_mask = eval('0b' + tristatestring.replace('X','0'))
    and_mask = eval('0b' + tristatestring.replace('X','1'))
    return(or_mask, and_mask)

def line_parse(line):
    """
    >>> line_parse('mask = 1XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX0')
    ('mask', 34359738368, 68719476734)
    >>> line_parse('mem[12] = 28')
    ('mem', 12, 28)
    """
    lvalue, _, rvalue = line.partition(' = ')
    if lvalue == 'mask':
        om, am = mask_decode(rvalue)
        return 'mask', om, am
    else:
        addr=int(lvalue[4:-1])
        return 'mem', addr, int(rvalue)

class DockingComputer(object):
    """
    #>>> DockingComputer().run_program(EXAMPLE_DOCKING_PROGRAM).sum_memory()
    165
    """
    def __init__(elf):
        elf._masks = (0, pow(2, 35) - 1)
        elf._mem={}
    
    def sum_memory(elf):
        response = sum(elf._mem.values())
        print('{0:036b}'.format(elf._masks[0]))
        print('{0:036b}'.format(elf._masks[1]))
        print('{0:036b}'.format(response))
        
        return response

    def run_program(elf, lines):
        for op, a1, a2 in map(line_parse,lines):
            if op == 'mask':
                elf._masks=(a1,a2)
            elif op == 'mem':
                elf._mem[a1] = (a2 | elf._masks[0]) & elf._masks[1]
        return elf # for method chaining

def day14_1_solver(lines):
    """ helper function
    #>>> day14_1_solver(EXAMPLE_DOCKING_PROGRAM)
    165
    >>> day14_1_solver(['mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X','mem[0] = 11'])
    73
    >>> day14_1_solver(['mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X','mem[0] = 101'])
    101
    >>> day14_1_solver(['mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X','mem[0] = 0'])
    64
    """
    return  DockingComputer().run_program(lines).sum_memory()

def day14_1():
    """
    >>> day14_1()
    10056808196593
    """
    with open('day14input.txt', 'r') as fp:
        return DockingComputer().run_program(fp).sum_memory()

