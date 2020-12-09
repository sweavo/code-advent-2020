import day9input 

import day1_1

TEST_DATA=[
    35,
    20,
    15,
    25,
    47,
    40,
    62,
    55,
    65,
    95,
    102,
    117,
    150,
    182,
    127,
    219,
    299,
    277,
    309,
    576 ]


def find_first_invalid_xmas_code( input_buffer, preamble_length ):
    """
    >>> find_first_invalid_xmas_code( TEST_DATA, 5)
    127
    """
    for offset, candidate in enumerate(input_buffer[preamble_length:]):
        result = day1_1.find_pair(candidate, input_buffer[offset:offset+preamble_length])
        if result is None:
            return candidate
       
def day9_1():
    """
    >>> day9_1()
    776203571
    """
    return find_first_invalid_xmas_code(day9input.DATA_STREAM, 25)
