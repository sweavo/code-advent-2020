import day5_1

def find_the_gap1( values ):
    """
        Give the value one higher than any in the first group of sorted 
        contiguous values in the input.
        >>> find_the_gap1( [ 5,6,7,9,10 ] )
        8
        """
    offset = values[0]
    for index, value in enumerate(values):
        if value != index + offset:
            return index + offset

def day5_2():
    """
        >>> day5_2()
        0
        """
    sorted_ints = day5_1.sorted_pass_ids(day5_1.day5input.BOARDING_PASSES)
    return find_the_gap1( sorted_ints )

