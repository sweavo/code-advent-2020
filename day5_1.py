import day5input

def seat_code_to_binary( code ):
    """
        >>> seat_code_to_binary('FBFBBFFRLR')
        '0101100101'
        """
    return code.replace('F', '0').replace('B', '1').replace('L','0').replace('R','1')

def seat_code_to_id( code ):
    """
        >>> seat_code_to_id('FBFBBFFRLR')
        357
        """
    return int( seat_code_to_binary( code ), 2 )

def highest( codes ):
    """
        >>> highest( day5input.BOARDING_PASSES )
        888
        """
    return sorted( map( seat_code_to_id, codes ))[-1]