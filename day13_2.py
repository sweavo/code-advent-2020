import functools
import operator
from math import gcd

import day13input

""" This is essentially a problem of combining period and phase of signals.

First, observe that the bus numbers are periods T_i, and that their positions
in the input are their offset c_i. (As presented, c_i == i but I will be 
reordering the buses below.) Solutions are found where 

    y = ( x + c ) % T

crosses zero. So solutions can only exist at:

    x = ( i * T ) - c for integer i

If we start with the largest period, we are leaping towards the solution in the
shortest number of steps. So I tag the buses with their indexes (now, offsets)
and sort them by period. When I consider the first two signals together, I know
that the solution if any occurs at a period T_r = lcm(T_0, T_1) and that gives
me an upper bound for finding the point at which both f(T_0,c_0) and f(T_0,c_0)
are zero. The lower bound is the first solution of the larger curve, i.e. 
T_0 - c_0.

I tried to do some more mathing to calculate the number of cycles of T_0 needed
to reach that solution based on the phase and period relationships of the two
signals, but I was defeated and had to go lie down just to recover the ability
to count or spell. So, I just brute-force by checking all values such that

    T_0-c_0 <= x < T_r-c_0  &&  x in ( T_0 * PositiveIntegers )

This solution is itself a signal, with period T_r and offset c_r where

    c_r = T_r - x found as above.

This means we just need a function to combine a longer with a shorter signal,
and we can apply it to the whole sequence of buses with functools.reduce()
"""

EXAMPLE_BUSES=[7, 13, None, None, 59, None, 31, 19]

def prep_input(buses):
    """ Sort the buses reversed by their period, having tagged them with their
    position in the sequence, which is their c value.
    >>> list(prep_input(EXAMPLE_BUSES))
    [(59, 4), (31, 6), (19, 7), (13, 1), (7, 0)]
    """
    return sorted([(bus, offset) 
                    for offset, bus 
                    in enumerate(buses) 
                    if bus], reverse=True)

def lcm(x, y):
    """ period of combined signal is lcm of the periods of its components
    >>> lcm(3, 9)
    9
    >>> lcm(4, 9)
    36
    """
    return x*y//gcd(x,y)

def combine_signals(longer,shorter):
    """ 
    >>> combine_signals((5,2), (3,1))
    (15, 7)
    >>> combine_signals((3,1), (2,0))
    (6, 4)
    >>> combine_signals((13,1),(12,0))
    (156, 144)
    """
    T_0, c_0 = longer
    T_1, c_1 = shorter

    # Period is the lcm of the provided periods
    T_result = lcm(T_0,T_1)
    
    # Determine phase by searching soutions of longer that fall between the
    # start position and start + T_result
    for i in range(T_0-c_0,T_result+c_0,T_0):
        v0 = (i + c_0) % T_0
        v1 = (i + c_1) % T_1
        if not( v0 or v1):
            return (T_result,T_result-i)

def solve_buses(prepared_buses):
    """ Reduce a bunch of periodic signals to a single signal. The value of x
    that answers the puzzle is the first place ( c + x ) % T = 0, that is to
    say, c + x = T, or x = T-c.
    >>> solve_buses(prep_input(EXAMPLE_BUSES))
    1068781
    """
    T, c = functools.reduce(combine_signals, prepared_buses)
    return T - c

def day13_2():
    """
    >>> day13_2()
    539746751134958
    """
    return solve_buses(prep_input(day13input.BUSES[1]))

