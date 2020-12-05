import day5_1

""" Insights:
        The pass IDs are just binary numbers: if B and R are 1 and F and L are 
        0 then you are just evaluating a 10-bit binary integer to derive the 
        pass ID.

        We know that the whole plane is full, though the integers do not 
        necessarily start at 0 nor extend to MAX_10BIT_UINT.  We know that the
        number we're seeking is not at either end of the range. So we have two
        contiguous blocks of integers separated by a single missing int, but 
        presented to us shuffled.

        What's a good way to find a discontinuity within a dataset that is 
        otherwise contiguous?

        sort it, and find the first number out of sequence.
"""

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
        522
        """
    sorted_ints = day5_1.sorted_pass_ids(day5_1.day5input.BOARDING_PASSES)
    return find_the_gap1( sorted_ints )

