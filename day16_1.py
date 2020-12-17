import day16input

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
    [(1, 3), (5, 7)]
    """
    name, _, ranges_text = rule.partition(': ')
    range_texts = ranges_text.split(' or ')
    ranges = list(map(lambda s: tuple(map(int, s.split('-'))),range_texts))
    return ranges

def read_rules(rules):
    return list(map(parse_rule, rules))

def validate_number(number, rules):
    for rule in rules:
        for rule_let in rule:
            if number>=rule_let[0] and number<=rule_let[1]:
                return True
    return False

def get_invalid_numbers_from_ticket(numbers, rules):
    for number in numbers:
        if not validate_number(number, rules):
            yield number

def get_invalid_numbers_from_tickets(tickets, rules):
    for ticket in tickets:
        for result in get_invalid_numbers_from_ticket(ticket, rules):
            yield result

def day16_1solver(rules, tickets):
    """
    >>> day16_1solver(RULES, TICKETS)
    71
    """
    rules = read_rules(rules)
    return sum(get_invalid_numbers_from_tickets(tickets, rules))

def day16_1():
    """
    >>> day16_1()
    20091
    """
    return day16_1solver(day16input.RULES, day16input.NEARBY_TICKETS)

