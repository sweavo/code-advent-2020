
EXAMPLE_RULES=[
    '0: 4 1 5',
    '1: 2 3 | 3 2',
    '2: 4 4 | 5 5',
    '3: 4 5 | 5 4',
    '4: "a"',
    '5: "b"' ]

EXAMPLE_STRINGS=[
    'ababbb',
    'bababa',
    'abbbab',
    'aaabbb',
    'aaaabbb' ]


def prepare_rules(rule_strings):
    """
    >>> r=prepare_rules(['0: 1', '1: 2 | 3 4', '3: "a"', '4: "b"'])
    >>> r.keys()
    dict_keys([0, 1, 3, 4])
    >>> r[0]
    ([1],)
    >>> r[1]
    ([2], [3, 4])
    >>> r[3]
    (['a'],)
    """ 
    output={}
    for key, _, production in map(lambda a: a.partition(': '), rule_strings):
        alternatives = production.split(' | ')
        sequences = []
        for alternative in alternatives:
            sequence = list(map(eval,alternative.split(' ')))
            sequences.append(sequence)
        output[int(key)] = tuple(sequences)
    return output
