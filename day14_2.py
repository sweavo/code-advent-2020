""" Writing through partially-unbound addresses

The main blocker is the ability to store values at addresses that are unbound,
e.g., addres 11X01XX means "all 7 addresses whose ones and zeroes match" and
this theoretically can mean many more addresses.

Design is to use a tree-like digraph of binary references (implemented as lists)
where each list represents the next bit in the address. When an X is encountered
we write to both branches, which is what stops it being a tree.

"""

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
        >>> g['1X0']
        0
        >>> g['100']
        6
        >>> g['110']
        6
        >>> g['101']
        0
        >>> g['111'] 
        2
        """
        if 'X' in key:
            cut = key.index('X')
            elf[key[:cut] + '0' + key[cut+1:]]=value
            elf[key[:cut] + '1' + key[cut+1:]]=value

        else:
            elf._memory[key]=value

    def __getitem__(elf,key):
        """ read through subscripti
        >>> g=GlobMemory()
        >>> g['10'] = 20
        >>> g['10']
        20
        >>> g['11'] # default is zero
        0
        """
        return elf._memory.get(key,0)
