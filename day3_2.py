import functools, operator

from day3_1 import MAP_FRAGMENT, count_slope
from day3input import DAY3_INPUT

SLOPES =  [ (1,1), (3,1), (5,1), (7,1), (1,2) ]
def enumerate_slopes( map_fragment, slopes ):
    """ 
    >>> list( enumerate_slopes( MAP_FRAGMENT, SLOPES ) )
    [2, 7, 3, 4, 2]
    """
    for slope in slopes:
        yield count_slope( map_fragment, slope)

def tree_product( map_fragment, slopes ):
    """
    >>> tree_product( MAP_FRAGMENT, SLOPES ) 
    336
    """
    return functools.reduce( operator.mul, enumerate_slopes( map_fragment, slopes ) )

def day3_2():
    """
    >>> day3_2()
    2265549792
    """
    return tree_product( DAY3_INPUT, SLOPES )

