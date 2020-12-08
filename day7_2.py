import collections
import re

import day7input

EXAMPLE_RULES = [
    "light red bags contain 1 bright white bag, 2 muted yellow bags.",
    "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
    "bright white bags contain 1 shiny gold bag.",
    "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
    "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
    "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
    "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
    "faded blue bags contain no other bags.",
    "dotted black bags contain no other bags." ]

EXAMPLE_RULES2 = [
    "shiny gold bags contain 2 dark red bags.",
    "dark red bags contain 2 dark orange bags.",
    "dark orange bags contain 2 dark yellow bags.",
    "dark yellow bags contain 2 dark green bags.",
    "dark green bags contain 2 dark blue bags.",
    "dark blue bags contain 2 dark violet bags.",
    "dark violet bags contain no other bags." ]

""" insights:

I'm rewriting part1 because we now need to care about the number of bags needed.
"""

RE_FIND_COUNTS=re.compile('(\d+)\s([\w ]+?)\sbags?')

def parse_rule( rule ):
    """ convert English rule into a tuple representing the grammar production
    >>> parse_rule( "light red bags contain 1 bright white bag, 2 muted yellow bags." )
    ('light red', {'bright white': 1, 'muted yellow': 2})
    >>> parse_rule( "dark orange bags contain 3 bright white bags, 4 muted yellow bags." )
    ('dark orange', {'bright white': 3, 'muted yellow': 4})
    >>> parse_rule( "bright white bags contain 1 shiny gold bag." )
    ('bright white', {'shiny gold': 1})
    >>> parse_rule( "faded blue bags contain no other bags." )
    ('faded blue', {})
    """
    key, _sep, tail = rule.partition(' bags contain ')
    colors = RE_FIND_COUNTS.findall( tail )
    return key, dict(map(lambda tup: (tup[1],int(tup[0])), colors))

def parse_rules( rules ):
    """ take list of strings with english rules and return dict of productions
    >>> parse_rules( [ "light red bags contain 1 bright white bag, 2 muted yellow bags.",
    ...     "dark orange bags contain 3 bright white bags, 4 muted yellow bags." ] )
    {'light red': {'bright white': 1, 'muted yellow': 2}, 'dark orange': {'bright white': 3, 'muted yellow': 4}}
    """
    return dict(map(parse_rule, rules))

def count_contents( paths, bag_color ):
    """ recursively total the descendants of a bag color
    >>> count_contents({'a': {'b': 1}}, 'a')
    1
    >>> count_contents({'a': {'b': 1}}, 'b')
    0
    >>> count_contents({'a': {'b': 1, 'c': 1}}, 'a')
    2
    >>> count_contents({'a': {'b': 1}, 'b': {'c': 1}}, 'a')
    2
    >>> count_contents({'a': {'b': 2}, 'b': {'c': 1}}, 'a')
    4
    >>> count_contents({'a': {'b': 1, 'c':2}, 
    ...                 'b': {'d': 3},
    ...                 'c': {'d': 4}}, 'a')
    14
    """
    def recurse( c_n_tuple ):
        """ return the total bags contained within n bags of color c. """
        color, multiple = c_n_tuple
        return multiple * (sum(map(recurse,paths.get(color,{}).items())) + 1)
    
    # At the top level, we have one bag, and we are not counting it in the answer.
    return recurse( (bag_color,1) )-1

def count_bags_in_bag( rules, color ):
    """ how many bags are necessarily contained in the bag of color color?
    >>> count_bags_in_bag( EXAMPLE_RULES, 'shiny gold' )
    32
    >>> count_bags_in_bag( EXAMPLE_RULES2, 'shiny gold' )
    126
    """
    return count_contents( parse_rules(rules), color )

def day7_2():
    """
    >>> day7_2()
    30899
    """
    return count_bags_in_bag( day7input.BAGGAGE_RULES, 'shiny gold' )

