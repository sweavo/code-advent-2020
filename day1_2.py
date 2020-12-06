from functools import reduce
import operator

import day1input
from day1_1 import valid_entries, find_pair

def fix_report_2( target, entries ):
    """ day 1.2 puzzle 
    >>> fix_report_2( 2020, [1721, 979, 366, 299, 675, 1456])
    241861950
    """
    return reduce( operator.mul, find_triple( target, entries ) )

def find_triple( target, entries ):
    """
    >>> find_triple(2020, [1721, 979, 366, 299, 675, 1456])
    (979, 675, 366)
    """
    for first in sorted(valid_entries(target,entries),reverse=True):
        subtarget = target-first
        try:
            second, third = find_pair(subtarget, entries)
            return (first, second, third )
        except TypeError:
            pass

def day1_2():
    """
    >>> day1_2()
    76110336
    """
    return fix_report_2(2020, day1input.REPORT )

