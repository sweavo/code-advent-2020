import re
import functools

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


class BasePolicy( object ):

    _RE_READ_POLICY = re.compile('(\d+)-(\d+)\s+(\w)$')

    @staticmethod
    def split_policystring( policy_string ):
        items = BasePolicy._RE_READ_POLICY.match( policy_string ).groups()
        return (int(items[0]), int(items[1]), items[2])

    def __init__( self, policy_string ):
        self._first, self._second, self._letter = BasePolicy.split_policystring( policy_string )


class Policy( BasePolicy ):
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
        super().__init__( policy_string )
        self._minimum = self._first
        self._maximum = self._second

    def validate( self, password ):
        """
            Rule: there must be between n and m occurrences of the letter
            >>> Policy('1-3 a').validate( 'ab' )
            True
            >>> Policy('1-3 b').validate( 'abb' )
            True
            >>> Policy('1-3 a').validate( 'aaa' )
            True
            >>> Policy('3-3 a').validate( 'ab' )
            False
            >>> Policy('3-3 b').validate( 'abb' )
            False
            >>> Policy('3-3 a').validate( 'aaa' )
            True
            >>> Policy('1-2 a').validate( 'ab' )
            True
            >>> Policy('1-2 b').validate( 'abb' )
            True
            >>> Policy('1-2 a').validate( 'aaa' )
            False
        """
        letter_count =  count_letter(self._letter, password )
        return self._minimum<=letter_count and letter_count<=self._maximum

def validate_password_line( policy_class, text ):
    """
    """
    policy_string, password = read_password_line(text)
    return policy_class(policy_string).validate( password )

def count_valid_password_lines( policy_class, password_file ):
    line_validator = functools.partial( validate_password_line, policy_class )
    iter_valid_lines = filter( line_validator, day2input.PASSWORD_FILE )
    return len( list(iter_valid_lines))

if __name__ == "__main__":
    print( count_valid_password_lines( Policy, day2input.PASSWORD_FILE ))
