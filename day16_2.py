import functools
import operator

import day16input
""" Design:

A function takes a ticket and a ruleset and returns a list of sets of possible field names.

If any of those sets is empty, the ticket is discarded as invalid.

The valid tickets' sets of possible fieldnames is then intersected with the previous until
all tickets have been consumed.
"""

RULES=[
    "class: 1-3 or 5-7",
    "row: 6-11 or 33-44",
    "seat: 13-40 or 45-50" ] 

TICKETS=[
    [7, 3, 47],
    [40, 4, 50],
    [55, 2, 20],
    [38, 6, 12] ]

def parse_rule(rule):
    """ ugh
    >>> parse_rule('class: 1-3 or 5-7')
    ((1, 3), (5, 7), 'class')
    """
    name, _, ranges_text = rule.partition(': ')
    range_texts = ranges_text.split(' or ')
    ranges = list(map(lambda s: tuple(map(int, s.split('-'))),range_texts))
    return ranges[0], ranges[1], name

class Validator(object):
    """ encapsulate a ruleset so that it can be used in map, etc.
    """
    def __init__(elf, rules):
        elf._rules = list(map(parse_rule, rules))

    def validate_number(elf, number):
        """
        >>> vv = Validator(RULES)
        >>> vv.validate_number(3)
        {'class'}
        >>> vv.validate_number(4)
        set()
        >>> sorted(vv.validate_number(6))
        ['class', 'row']
        """
        possible_fields=set()
        for rule in elf._rules:
            for rule_let in rule[:2]:
                if number>=rule_let[0] and number<=rule_let[1]:
                    possible_fields.add(rule[2])
        return possible_fields
       
    def validate_ticket(elf, ticket):
        return list(map(elf.validate_number, ticket))

    def generate_valid_resultsets(elf, tickets):
        for result in map(elf.validate_ticket,tickets):
            if set() not in result:
                yield result


def multiplex_intersect(sets1, sets2):
    """ given two sequences of sets, return the sequence of the intersects of 
    the sets.
    >>> multiplex_intersect([{1,5},{2},{6,8,9}], [{2,5,6},{1},{5,6}])
    [{5}, set(), {6}]
    """
    return list(map(set.intersection,sets1, sets2))

def eliminate_dups(sets):
    """ given a sequence of sets, some of which are singletons, remove the singletons 
    from the non-singleton sets until stability reached
    >>> eliminate_dups([{1,2,3},{1,2},{1}])
    [3, 2, 1]
    """
    changes_due=True
    while changes_due:
        changes_due=False
        decided_values = [list(s)[0] for s in sets if len(s) == 1]
        for value in decided_values:
            for ss in sets:
                if len(ss)>1 and value in ss:
                    changes_due=True
                    ss.remove(value)
    return list(map(lambda s: list(s)[0], sets))

def find_fields(rules, tickets):
    """
    >>> find_fields(RULES, TICKETS)
    ['row', 'class', 'seat']
    """
    vv = Validator(rules)
    fields=functools.reduce(multiplex_intersect, vv.generate_valid_resultsets(tickets))
    return eliminate_dups(fields) 

def indices_matching(seq, fun):
    for i, val in enumerate(seq):
        if fun(val):
            yield i

def day16_2():
    """
    >>> day16_2()
    2325343130651
    """
    fields = find_fields(day16input.RULES, day16input.NEARBY_TICKETS)
    indices = indices_matching(fields, lambda s: s.startswith('departure'))
    answers = map(day16input.MY_TICKET.__getitem__, indices)
    return functools.reduce(operator.mul, answers)
    
