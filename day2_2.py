import re

import day2input
from day2_1 import count_letter, read_password_line

def extract_letters( idx1, idx2, text ):
    """
        >>> extract_letters( 0, 3, 'hi there')
        'ht'
        >>> extract_letters( 5, 5, 'abcdef' )
        'ff'
    """
    return text[idx1] + text[idx2]


class Policy( object ):

    RE_READ_POLICY = re.compile('(\d+)-(\d+)\s+(\w)$')

    def __init__(self, policy_string ):
        """
            >>> p=Policy('1-3 b')
            >>> p._index1
            0
            >>> p._index2
            2
            >>> p._letter
            'b'
        """
        items = self.RE_READ_POLICY.match( policy_string ).groups()
        self._index1 = int(items[0])-1 # corrected for zero-based indexes
        self._index2 = int(items[1])-1 # corrected for zero-based indexes
        self._letter = items[2]

    def validate( self, password ):
        """
            >>> Policy('1-3 b').validate( 'abb' )
            True
            >>> Policy('1-3 a').validate( 'aaa' )
            False
        """
        check_letters = extract_letters(self._index1, self._index2, password)
        return 1 == count_letter(self._letter, check_letters )

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
    policy_string, password = read_password_line(text)
    return Policy(policy_string).validate( password )

if __name__ == "__main__":
    print( len( list(filter( validate_password_line, day2input.PASSWORD_FILE ))))