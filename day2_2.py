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
    """ take a line from the password file and return the two indices (corrected to be zero-based), letter, and password.
        >>> read_password_line( '1-2 x: bibble')
        (0, 1, 'x', 'bibble')
    """
    items =  RE_READ_PASSWORD_LINE.match(text).groups()
    return (int(items[0])-1, int(items[1])-1, items[2], items[3] )

def extract_letters( idx1, idx2, password ):
    """
        >>> extract_letters( 0, 3, 'hi there')
        'ht'
        >>> extract_letters( 5, 5, 'abcdef' )
        'ff'
    """
    return password[idx1] + password[idx2]

def validate_password_line( text ):
    """
        Rule: exactly one of the two given indices must contain the given letter (1-based!)
        >>> validate_password_line( '1-3 a: abc' )
        True
        >>> validate_password_line( '1-3 b: abb' )
        True
        >>> validate_password_line( '1-3 a: aaa' )
        False
        >>> validate_password_line( '3-3 a: bab' )
        False
        >>> validate_password_line( '3-3 b: abb' )
        False
        >>> validate_password_line( '3-3 a: aaa' )
        False
        >>> validate_password_line( '1-2 a: ab' )
        True
        >>> validate_password_line( '1-2 b: abb' )
        True
        >>> validate_password_line( '1-2 a: aaa' )
        False
    """
    index1, index2, letter, password = read_password_line(text)
    return 1 == count_letter(letter, extract_letters(index1, index2, password))
    

if __name__ == "__main__":
    print( len( list(filter( validate_password_line, day2input.PASSWORD_FILE ))))