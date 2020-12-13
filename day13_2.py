import functools
import operator

import day13input

""" For part 2 it feels like some math can avoid a lot of hacking.  This smells
like Seive of Eratosthenes. For example, solutions are not going to exist any
place except where x % buses[0] is zero. So a loop can step by buses[0].

In fact, solutions can only be at places where the longest period appears at 
its correct offset.  So a first pass can find offset, maxperiod and then look
for solutions at (maxperiod * i in POSITIVE_INTS) - offset
"""
x=None # "x" appears in the input data. This makes it valid syntactically

EXAMPLE_INPUT=(939,
    [7, 13, x, x, 59, x, 31, 19])

def prep_input(buses):
    """ Sort the buses by their reverse period, and add their position in the
    input, which is also the offset from the solution at which they will appear
    >>> list(prep_input(EXAMPLE_INPUT[1]))
    [(59, 4), (31, 6), (19, 7), (13, 1), (7, 0)]
    """
    return sorted([(bus, offset) for offset, bus in enumerate(buses) if bus], reverse=True)

""" In the first example above, our first candidate is at 55, since it is 4 minutes before the 59 arrives.  Is it also 6 minutes before 31 arrives? No, it's 7 minutes before that, so ... next candidate is 55+59=114...
"""

def check_answer(buses, timestamp):
    """ Do all the listed buses leave at the offsets given from timestamp?
    >>> check_answer(prep_input([17,x,13,19]), 3400)
    False
    >>> check_answer(prep_input([17,x,13,19]), 3417)
    True
    >>> check_answer(prep_input([67,7,59,61]), 754018)
    True
    >>> check_answer(prep_input([67,x,7,59,61]), 779210)
    True
    >>> check_answer(prep_input([67,7,x,59,61]), 1261476)
    True
    >>> check_answer(prep_input([1789,37,47,1889]), 1202161486)
    True
    """
    for mod, offs in buses:
        if ( timestamp + offs ) % mod:
            return False
    return True


