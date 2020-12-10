""" problem:

I leapt to a recursive descent to enumerate the potentially 3^n solutions. 
Starting with the node with value 0, we sum the trees found at 1, 2, and/or 3.
This continues until we reach the end (return a sum) or have no more options
(return None to backtrack).

I feel like there's an insight to be had around the idea that it's not a tree
because it converges as well as diverges, i.e., there are multiple ways to 
reach node X so node X's path count can be re-used.  This reminds me of an
earlier puzzle in AoC2020.

Is this the shiny gold bag problem?

No, because paths here only terminate when they reach the goal.

So... looking at reusing answers, does it make sense to walk the list backwards?

Yes: the highest-numbered joltage (assuming it is >=target-3) has 1 way to reach
the device, then the next highest has, for each of its reachable numbers, the 
sum of their ways to eventually reach the goal.

Why search backwards rather than forwards? Not sure. As I try to explain that,
I get stuck. I think that in either direction, an unreachable value will result
in the partial sum being correctly discarded. I'll start the implementation in 
the forward direction and see what the tests tell me.
"""

import day10_1

import day10input

def walk_window(sequence, max_interval=3):
    """ yield pairs of indices into sequence whose values are within max_interval
    >>> list(walk_window([0,1,2,3,4,6,9]))
    [(0, 1), (0, 2), (0, 3), (1, 4), (3, 5), (5, 6)]
    """
    tail_index=0
    for head_index, head in enumerate(sequence[1:],1):
        while sequence[tail_index] < head - 3:
            tail_index+=1
        yield(tail_index, head_index)

def prepare_sequence(bag):
    """ given a set of adaptor voltages, plug them in to the outlet (0) and the
    device (max+3)
    >>> target, sequence = prepare_sequence([4,2,5])
    >>> target
    8
    >>> sequence
    [0, 2, 4, 5, 8]
    """
    bag.append(0) # add in the origin
    sequence=sorted(bag) 
    target=sequence[-1]+3
    sequence.append(target)
    return target, sequence

def count_routes(sequence):
    """ Starting at 0, how many ways are there to reach max+3 making leaps of 1..3?
    >>> count_routes(day10_1.EXAMPLE1)
    8
    >>> count_routes(day10_1.EXAMPLE2)
    19208

    Design notes: 
    
    Tally's indices correspond to those in the sequence. walk_window can be 
    trusted to increment the leading index each iteration, so we can just append
    each time. python's lovely array slicing means that items[first:last]
    excludes items[last].

    The first member of tally is the outlet, that has one way to reach itself,
    so we initialize tally with [1].
    """
    target, sequence = prepare_sequence(sequence)

    tally=[1]

    for first, last in walk_window(sequence):
        tally.append(sum(tally[first:last]))

    return tally[-1]

def day10_2():
    """ let's try it with many permutations:
    >>> day10_2()
    3543369523456
    """
    return count_routes(day10input.ADAPTOR_RATINGS)

