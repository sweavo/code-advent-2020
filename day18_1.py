import operator

import day18input

class LEXEME(object):
    def __init__(self, name):
        self._name=name
    def __repr__(self):
        return self._name

def lex(expression_text):
    """
    >>> list(lex("3 + 2"))
    [3, '+', 2]
    >>> list(lex("3 + (2 * 2)"))
    [3, '+', '(', 2, '*', 2, ')']
    """
    for c in expression_text:
        if c in "0123456789": yield int(c)
        elif c in '+*()': yield c
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
        elif lex == '(':
            accum = op(accum, evaluate(lexeme_iterator))
        elif lex == ')':
            return accum
        elif lex in '+*':
            op=operator.mul if lex == '*' else operator.add
    return accum

def evaluate_strings(strings):
    return sum(map(evaluate, map(lex, strings))) 

def day18_1():
    """
    >>> day18_1()
    31142189909908
    """
    return evaluate_strings(day18input.EXPRESSIONS)

