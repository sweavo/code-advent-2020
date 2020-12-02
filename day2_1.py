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


def read_password_line(text):
    """
        >>> read_password_line('1-2 z: hello')
        ('1-2 z', 'hello')
    """
    return tuple(map(str.strip,text.split(':')))


class Policy( object ):

    RE_READ_POLICY = re.compile('(\d+)-(\d+)\s+(\w)$')

    def __init__(self, policy_string ):
        """
            >>> p=Policy('1-3 b')
            >>> p._minimum
            1
            >>> p._maximum
            3
            >>> p._letter
            'b'
        """
        items = self.RE_READ_POLICY.match( policy_string ).groups()
        self._minimum = int(items[0])
        self._maximum = int(items[1])
        self._letter = items[2]

    def validate( self, password ):
        """
            >>> Policy('1-3 b').validate( 'abb' )
            True
            >>> Policy('1-3 a').validate( 'aaa' )
            True
        """
        letter_count =  count_letter(self._letter, password )
        return self._minimum<=letter_count and letter_count<=self._maximum

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
    policy_string, password = read_password_line(text)
    return Policy(policy_string).validate( password )

if __name__ == "__main__":
    print( len( list(filter( validate_password_line, day2input.PASSWORD_FILE ))))