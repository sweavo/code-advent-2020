"""
expr = factor '*' expr | factor
factor = term '+' factor | term
term = '(' expr ')' | const
const = int
"""
import operator

import day18input
import day18_1

class Lookaheader(object):
    def __init__(self,iterator):
        self._it = iterator
        self._lookahead = iterator.__next__()

    def peek(self):
        return self._lookahead

    def take(self):
        ret = self._lookahead
        self._lookahead = self._it.__next__()
        return ret

def parse_expr(source):
    """
    >>> parse_expr(Lookaheader(day18_1.lex('3')))
    3
    >>> parse_expr(Lookaheader(day18_1.lex('3 + 2')))
    ('+', 3, 2)
    >>> parse_expr(Lookaheader(day18_1.lex('3 * 2')))
    ('*', 3, 2)
    >>> parse_expr(Lookaheader(day18_1.lex('3 * 2 + 4')))
    ('*', 3, ('+', 2, 4))
    >>> parse_expr(Lookaheader(day18_1.lex('3 * (2 + 4)')))
    ('*', 3, ('+', 2, 4))
    >>> parse_expr(Lookaheader(day18_1.lex('(3 * 2) + 4')))
    ('+', ('*', 3, 2), 4)
    """
    lhs = parse_factor(source)
    if source.peek() == '*':
        source.take()
        rhs = parse_expr(source)
        return ('*', lhs, rhs)
    else:
        return lhs

def parse_factor(source):
    lhs = parse_term(source)
    if source.peek() == '+':
        source.take()
        rhs = parse_factor(source)
        return ('+', lhs, rhs)
    else:
        return lhs

def parse_term(source):
    ahead = source.take()
    if ahead == '(':
        lhs = parse_expr(source)
        source.take() # throw away closing paren
        return lhs
    elif isinstance(ahead,int):
        return ahead

def evaluate(parsed):
    """
    >>> evaluate(parse_expr(Lookaheader(day18_1.lex('3 * 2 + 4'))))
    18
    """
    if isinstance(parsed,int):
        return parsed
    else:
        fn = operator.add if parsed[0] == '+' else operator.mul
        return fn(*map(evaluate, parsed[1:]))

def eval_string_expr(string):
    """
    >>> eval_string_expr('1 + (2 * 3) + (4 * (5 + 6))')
    51
    >>> eval_string_expr('2 * 3 + (4 * 5)')
    46
    >>> eval_string_expr('5 + (8 * 3 + 9 + 3 * 4 * 3)')
    1445
    >>> eval_string_expr('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))')
    669060
    >>> eval_string_expr('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2')
    23340
    """ 
    return evaluate(parse_expr(Lookaheader(day18_1.lex(string))))

def day18_2():
    """
    >>> day18_2()
    323912478287549
    """
    return sum(map(eval_string_expr, day18input.EXPRESSIONS))
