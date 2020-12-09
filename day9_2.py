import day9input
import day9_1

""" After having some faulty insights, I am just going to brute force this.

Mistakes made during design: assuming the sequence increases monotonically. It
doesn't, though it does _tend_ to increase. This led to stopping the search as
soon as a value greater than our target was found, which excluded possibilities.

"""
def pontoon( target, cards ):
    """ find a contiguous sequence of cards that sum to target, returning their indices
    >>> cards = [1, 10, 9, 2, 5]
    >>> target=20
    >>> pontoon(target, cards)
    3
    >>> target
    20
    >>> pontoon(21, cards)
    >>> pontoon(21, cards[1:])
    3
    >>> pontoon(21, cards[2:])
    """
    for index, candidate in enumerate(cards):
        target-=candidate
        if target==0:
            return index+1

def meta_pontoon( target, cards ):
    """ find a contiguous sequence of cards that sum to target, returning their indices
    >>> cards = [1, 10, 9, 2, 5]
    >>> meta_pontoon(21, cards)
    (1, 4)
    >>> cards[1:4]
    [10, 9, 2]
    >>> meta_pontoon(16, cards)
    (2, 5)
    """
    for start in range(len(cards)):
        result = pontoon(target,cards[start:])
        if result:
            return start, start+result
        
def puzzle_answer( target, cards ):
    """
    >>> puzzle_answer(127, day9_1.TEST_DATA)
    62
    """
    start, stop = meta_pontoon( target, cards )
    ordered_cards = sorted(cards[start:stop])
    return ordered_cards[0] + ordered_cards[-1]

def day9_2():
    """
    >>> day9_2()
    104800569
    """
    return puzzle_answer( day9_1.day9_1(), day9input.DATA_STREAM )

