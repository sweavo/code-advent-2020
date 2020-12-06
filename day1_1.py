import  day1input 

def find_pair( target, entries ):
    """ Find two elements of entries that sum to target
    >>> find_pair(2020, [1721, 979, 366, 299, 675, 1456])
    (1721, 299)
    """
    for left in sorted(valid_entries( target, entries ),reverse=True):
        right = target-left
        if right in entries:
            return left, right


def valid_entries( target, entries ):
    """ Remove entries from the list that exceed target, to reduce search space
    >>> valid_entries( 1000, [1721, 979, 366, 299, 675, 1456])
    [979, 366, 299, 675]
    """
    return list(filter(lambda x: x<=target, entries ))

def fix_report( entries ):
    """find the pair of entries that sum to 2020, and multiply them.
    (day 1.1 puzzle)

    >>> fix_report([1721, 979, 366, 299, 675, 1456])
    514579
    """
    terms=find_pair(2020, entries)
    return terms[0] * terms[1]

def day1_1():
    """
    >>> day1_1()
    889779
    """
    return fix_report( day1input.REPORT )

