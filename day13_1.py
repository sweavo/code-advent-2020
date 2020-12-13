import functools
import operator

import day13input

x=None # "x" appears in the input data. This makes it valid syntactically

EXAMPLE_INPUT=(939,
    [7,13,x,x,59,x,31,19])

def wait_time( timestamp, bus ):
    """ Modulo, but subtracted from the modulus, to give minutes remaining
    >>> wait_time( 939, 7 )
    (7, 6)
    >>> wait_time( 939, 59 )
    (59, 5)
    """
    return bus, bus-(timestamp%bus)

def wait_times( timestamp, buses ):
    """
    >>> list(wait_times(*EXAMPLE_INPUT))
    [(7, 6), (13, 10), (59, 5), (31, 22), (19, 11)]
    """
    fn = functools.partial(wait_time, timestamp)
    return map(fn,filter(lambda b: b is not None, buses))

def day13_1_solver(timestamp, buses):
    """
    >>> day13_1_solver(*EXAMPLE_INPUT)
    295
    """
    answers=sorted(list(wait_times(timestamp, buses)),key=lambda t: t[1])
    return operator.mul(*answers[0])

def day13():
    """
    >>> day13()
    171
    """
    return day13_1_solver(*day13input.BUSES)

