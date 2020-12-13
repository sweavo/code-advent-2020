import functools
import operator
from math import gcd

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
    Return the index of the first wrong answer, or len(buses) for OK
    >>> check_answer(prep_input([17,x,13,19]), 3400)
    0
    >>> check_answer(prep_input([17,x,13,19]), 3417)
    3
    >>> check_answer(prep_input([67,7,59,61]), 754018)
    4
    >>> check_answer(prep_input([67,x,7,59,61]), 779210)
    4
    >>> check_answer(prep_input([67,7,x,59,61]), 1261476)
    4
    >>> check_answer(prep_input([1789,37,47,1889]), 1202161486)
    4
    """
    for i, bus in enumerate(buses):
        mod, offs = bus
        if ( timestamp + offs ) % mod:
            return i
    return i + 1

""" Thinking about interference patterns, two periods shift phase over a certain
period too. The period of that phase shift relates to the longer period and the reciprocal of the difference in periods.

In fact, each incorrect result can know how many leaps it will take to match
the longest period. So we can treat it like a combination lock with a tension
wrench: find the period of the first item, check the second, derive a new 
period to search so that the foregoing items are correct.

        ** coffee, bagel, and an hour playing with the cat later **

There are two ways to look at it, a set intersection of the zero crossing
points of each signal, or period and phase of each signal.  Taking the period
and phase view, we start with the longest period and find the first point 
indicated by its phase (=period-offset), then check the signal of the next 
highest period. If that's not at the correct offset, we keep adding period 
until it locks in.  Then our new period is lcm( period, period_new ) and we 
proceed with checking the next item.
"""
def lcm(x, y):
    """
    >>> lcm(3, 9)
    9
    >>> lcm(4, 9)
    36
    """
    return x*y//gcd(x,y)

def combine_signals(longer,shorter):
    """ Each signal is a period, phase tuple. Return another period, phase
    tuple for the combination. tuple is (t,c) and signal is y = (x+c)%t. For
    all signals, the correct answer x is where y is zero.
    >>> combine_signals((5,2), (3,1))
    (15, 7)
    >>> combine_signals((3,1), (2,0))
    (6, 4)
    >>> combine_signals((13,1),(12,0))
    (156, 144)
    """
    t0, c0 = longer
    t1, c1 = shorter

    # Period is the lcm of the provided periods
    tr = lcm(t0,t1)
    # Search for phase within the first new period from the start position
    for i in range(t0-c0,tr+c0,t0):
        v0 = (i + c0) % t0
        v1 = (i + c1) % t1
        if not( v0 or v1):
            return (tr,tr-i)

def solve_buses(prepared_buses):
    """
    >>> solve_buses(prep_input(EXAMPLE_INPUT[1]))
    1068781
    """
    t,c = functools.reduce(combine_signals, prepared_buses)
    return t-c

def day13_2():
    """
    >>> day13_2()
    539746751134958
    """
    return solve_buses(prep_input(day13input.BUSES[1]))


