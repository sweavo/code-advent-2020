import operator

import day18input

class LEXEME(object):
    def __init__(self, name):
        self._name=name
    def __repr__(self):
        return self._name

OPAR=LEXEME('OPAR')
CPAR=LEXEME('CPAR')

def lex(expression_text):
    """
    >>> list(lex("3 + 2"))
    [3, <built-in function add>, 2]
    >>> OPAR == CPAR
    False
    >>> list(lex("3 + (2 * 2)"))
    [3, <built-in function add>, OPAR, 2, <built-in function mul>, 2, CPAR]
    """
    for c in expression_text:
        if c in "0123456789": yield int(c)
        elif c == '+': yield operator.add
        elif c == '*': yield operator.mul
        elif c == '(': yield OPAR
        elif c == ')': yield CPAR
        elif c == ' ': pass
        else: raise ValueError(f'do not know what to do with "{c}".')

def evaluate(lexeme_iterator):
    """
    >>> evaluate(lex('3 + 2'))
    5
    >>> evaluate(lex('3 + 2 * 4'))
    20
    >>> evaluate(lex('(3 + 2) * 4'))
    20
    >>> evaluate(lex('3 + (2 * 4)'))
    11
    >>> evaluate(lex('2 * 3 + (4 * 5)'))
    26
    >>> evaluate(lex('5 + (8 * 3 + 9 + 3 * 4 * 3)'))
    437
    >>> evaluate(lex('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'))
    12240
    >>> evaluate(lex('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'))
    13632
    """
    accum=0
    op=operator.add
    for lex in lexeme_iterator:
        if isinstance(lex, int):
            accum = op(accum, lex)
        elif lex == OPAR:
            accum = op(accum, evaluate(lexeme_iterator))
        elif lex == CPAR:
            return accum
        elif lex in [operator.mul, operator.add]:
            op=lex
    return accum

def evaluate_strings(strings):
    return sum(map(evaluate, map(lex, strings))) 

def day18_1():
    """
    >>> day18_1()
    31142189909908
    """
    return evaluate_strings(day18input.EXPRESSIONS)
