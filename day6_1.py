"""
I think I can reuse yield_records for this input

>>> res = list(day4_1.yield_records( EXAMPLE_INPUT ) )
>>> res[1]
'a b c'

"""

import itertools

import day4_1
import day6input

EXAMPLE_INPUT=[
    "abc",
    "",
    "a",
    "b",
    "c",
    "",
    "ab",
    "ac",
    "",
    "a",
    "a",
    "a",
    "a",
    "",
    "b" ]

def count_yeses( answers ):
    """ Count the unique, non-space characters in the answers string
    >>> count_yeses( 'a b c')
    3
    >>> count_yeses( 'a b a')
    2
    >>> count_yeses( 'abc')
    3
    """
    without_spaces=itertools.filterfalse( str.isspace,answers )
    uniques=set(without_spaces)
    return len(uniques)

def sum_survey( survey_records ):
    """ total the counts of unique answers given the extracted records 
    >>> sum_survey( ['abc','abc', 'abc', 'a', 'b' ] )
    11
    """
    return sum(map(count_yeses,survey_records))

def day6_1():
    """
    >>> day6_1()
    6590
    """
    return sum_survey( day4_1.yield_records( day6input.SURVEY ) )

