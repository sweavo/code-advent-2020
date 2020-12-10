""" the problem

It looks like the question of whether such a path exists is a red herring. It's
enough to sort the list of "joltages" and then count the intervals as we walk
up the values.  I can use the interval as an index to a dict and just increment
the value there.

python contains collections.Counter that encapsulates this semantic.
"""
import collections

import day10input

EXAMPLE1=[ 16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4 ]
EXAMPLE2=[ 28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3 ]

def intervals(sequence):
    """ generate the differences between consecutive elements of the sequence
    >>> list(intervals([0,1,3,5,8]))
    [1, 2, 2, 3]
    """
    return map(lambda tup: tup[1]-tup[0], zip(sequence[:-1],sequence[1:]))

def count_intervals(sequence):
    """ Tally the differences between consecutive items in sequence.
    (which must be ordered)
    >>> dict(count_intervals([0,1,4,5,7,10]))
    {1: 2, 3: 2, 2: 1}
    """
    return collections.Counter(intervals(sequence))

def test_joltage_adaptors(adaptor_set):
    """ The puzzle algorithm includes a 3-jolt interval for the last step
    >>> result=test_joltage_adaptors(EXAMPLE1)
    >>> result[1]
    7
    >>> result[3]
    5
    >>> result=test_joltage_adaptors(EXAMPLE2)
    >>> result[1]
    22
    >>> result[3]
    10
    """
    tally = count_intervals(sorted([0] + adaptor_set))
    # Add the 3-jolt interval for the device itself
    tally.update([3])
    return tally

def day10_1():
    """
    >>> day10_1()
    1984
    """
    results = test_joltage_adaptors(day10input.ADAPTOR_RATINGS)
    return results[1] * results[3]
