import  day1input 

def fix_report( entries ):
    """ day 1.1 puzzle

        >>> fix_report([1721, 979, 366, 299, 675, 1456])
        514579

    """
    terms=find_pair(2020, entries)
    return terms[0] * terms[1]

def find_pair( target, entries ):
    """ 
        >>> find_pair(2020, [1721, 979, 366, 299, 675, 1456])
        (1721, 299)
    """
    for left in sorted(valid_entries( target, entries ),reverse=True):
        right = target-left
        if right in entries:
            return left, right


def valid_entries( target, entries ):
    """
        >>> valid_entries( 1000, [1721, 979, 366, 299, 675, 1456])
        [979, 366, 299, 675]
    """
    return list(filter(lambda x: x<=target, entries ))

if __name__ == "__main__": # pragma: no cover
    print( fix_report( day1input.REPORT ) )

