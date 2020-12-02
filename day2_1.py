import re

import day2input

def count_letter( letter, haystack ):
    """
        >>> count_letter( 'a', 'aaa') 
        3
        >>> count_letter( 'a', 'abcabc' )
        2
        >>> count_letter( 'z', 'puzzle pizza' )
        4
        >>> count_letter( 'r','racecar' )
        2
    """
    return haystack.count( letter )

RE_READ_PASSWORD_LINE = re.compile('(\d+)-(\d+)\s+(\w):\s+([^\s]+)')
def read_password_line( text ):
    """ take a line from the password file and return min, max, letter, and password.
        >>> read_password_line( '1-2 x: bibble')
        (1, 2, 'x', 'bibble')
    """
    items =  RE_READ_PASSWORD_LINE.match(text).groups()
    return (int(items[0]), int(items[1]), items[2], items[3] )

def validate_password_line( text ):
    """
        >>> validate_password_line( '1-3 a: ab' )
        True
        >>> validate_password_line( '1-3 b: abb' )
        True
        >>> validate_password_line( '1-3 a: aaa' )
        True
        >>> validate_password_line( '3-3 a: ab' )
        False
        >>> validate_password_line( '3-3 b: abb' )
        False
        >>> validate_password_line( '3-3 a: aaa' )
        True
        >>> validate_password_line( '1-2 a: ab' )
        True
        >>> validate_password_line( '1-2 b: abb' )
        True
        >>> validate_password_line( '1-2 a: aaa' )
        False
    """
    minimum, maximum, letter, password = read_password_line(text)
    number_of_occurrences = count_letter(letter, password)
    return minimum <= number_of_occurrences and number_of_occurrences <= maximum

if __name__ == "__main__":
    print( len( list(filter( validate_password_line, day2input.PASSWORD_FILE ))))