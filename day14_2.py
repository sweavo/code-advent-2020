""" Writing through partially-unbound addresses

The main blocker is the ability to store values at addresses that are unbound,
e.g., addres 11X01XX means "all 7 addresses whose ones and zeroes match" and
this theoretically can mean many more addresses.

Design is to use a tree-like digraph of binary references (implemented as lists)
where each list represents the next bit in the address. When an X is encountered
we write to both branches, which is what stops it being a tree.

"""

EXAMPLE1=[
    "mask = 000000000000000000000000000000X1001X",
    "mem[42] = 100",
    "mask = 00000000000000000000000000000000X0XX",
    "mem[26] = 1 " ]

class GlobMemory(object):
    def __init__(elf):
        elf._memory = {}

    def __repr__(elf):
        """
        >>> GlobMemory()
        GlobMemory({})
        """
        return f'{elf.__class__.__name__}({elf._memory})'

    def __setitem__(elf,key,value):
        """ provide ability to write through subscript
        >>> g=GlobMemory()
        >>> g['10'] = 40
        >>> g['10']
        40
        >>> g['11X'] = 2 # test the globbing
        >>> g['1X0'] = 6
        >>> g['100']
        6
        >>> g['110']
        6
        >>> g['101']
        0
        >>> g['111'] 
        2
        >>> g.values()
        dict_values([40, 6, 2, 6])
        """
        if 'X' in key:
            cut = key.index('X')
            elf[key[:cut] + '0' + key[cut+1:]]=value
            elf[key[:cut] + '1' + key[cut+1:]]=value

        else:
            key=int(key,2)
            elf._memory[key]=value

    def __getitem__(elf,key):
        """ read through subscripti
        >>> g=GlobMemory()
        >>> g['10'] = 20
        >>> g['10']
        20
        >>> g[2] # btw integers are cool too
        20
        >>> g['11'] # default is zero
        0
        """
        if isinstance(key,str):
            key=int(key,2)
        return elf._memory.get(key,0)

    def values(elf):
        return elf._memory.values()

    def items(elf):
        return elf._memory.items()

def apply_mask(mask, address):
    """
    >>> apply_mask('10X0','0011')
    '10X1'
    """
    def bitdecision(tup):
        return tup[1] if tup[0]=='0' else tup[0]
    
    return ''.join(map(bitdecision, zip(mask, address)))

def parse_line(line):
    """
    >>> parse_line('mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X')
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X'
    >>> parse_line('mem[8] = 11')
    ('000000000000000000000000000000001000', 11)
    """
    op, _, arg = line.partition(' = ')
    if op == 'mask':
        return arg
    else:
        addr=int(op[4:-1])
        return '{0:036b}'.format(addr), int(arg)

def run_program(memory, lines):
    """
    >>> m=GlobMemory()
    >>> run_program(m, EXAMPLE1)
    >>> sum(m.values())
    208
    """
    mask='00000000000000000000000000000000000'
    for operation in map(parse_line, lines):
        if isinstance(operation,tuple):
            memory[apply_mask(mask,operation[0])] = operation[1]
        else:
            mask = operation

def day14_2():
    """
    >>> day14_2()
    2173858456958
    """
    memory = GlobMemory()
    with open('day14input.txt', 'r') as fp:
        run_program(memory, fp)
    return sum(memory.values())

