import functools

import day4_1
import day6_1
import day6input

def count_unanimous( answers ):
    """ count the characters that appear in all words in the input string.

    String must be words separated by a single space.

    >>> count_unanimous( 'a b a' ) # no letter appears in all three
    0
    >>> count_unanimous( 'abc ac ab') # 1: a
    1
    >>> count_unanimous( 'a' ) # a
    1
    >>> count_unanimous( 'frog dog bog' ) #2: o, g.
    2
    """
    sets = map(set, answers.split(' '))
    unanimous = functools.reduce( set.intersection, sets )
    return len(unanimous)
            
def day6_2():
    """
    >>> day6_2()
    3288
    """
    return day6_1.sum_survey( day4_1.yield_records( day6input.SURVEY ),
                       count_unanimous )

