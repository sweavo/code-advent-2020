import re
import functools

import day2input
from day2_1 import count_letter, read_password_line, validate_password_line, count_valid_password_lines, BasePolicy

def extract_letters( idx1, idx2, text ):
    """
        >>> extract_letters( 0, 3, 'hi there')
        'ht'
        >>> extract_letters( 5, 5, 'abcdef' )
        'ff'
    """
    return text[idx1] + text[idx2]


class Policy2( BasePolicy ):

    def __init__(self, policy_string ):
        """
            >>> p=Policy2('1-3 b')
            >>> p._index1
            0
            >>> p._index2
            2
            >>> p._letter
            'b'
        """
        super().__init__(policy_string)
        self._index1 = self._first-1 # corrected for zero-based indexes
        self._index2 = self._second-1 # corrected for zero-based indexes

    def validate( self, password ):
        """
            Rule: exactly one of the two given indices must contain the given letter (1-based!)
            >>> Policy2('1-3 a').validate( 'abc' )
            True
            >>> Policy2('1-3 b').validate( 'abb' )
            True
            >>> Policy2('1-3 a').validate( 'aaa' )
            False
            >>> Policy2('3-3 a').validate( 'bab' )
            False
            >>> Policy2('3-3 b').validate( 'abb' )
            False
            >>> Policy2('3-3 a').validate( 'aaa' )
            False
            >>> Policy2('1-2 a').validate( 'ab' )
            True
            >>> Policy2('1-2 b').validate( 'abb' )
            True
            >>> Policy2('1-2 a').validate( 'aaa' )
            False
        """
        check_letters = extract_letters(self._index1, self._index2, password)
        return 1 == count_letter(self._letter, check_letters )

if __name__ == "__main__": # pragma: no cover
    print( count_valid_password_lines( Policy2, day2input.PASSWORD_FILE ))
