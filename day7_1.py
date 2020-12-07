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

""" insights:

These are essentially grammar productions written in English. If we can 
compensate for plurals, then " bags contain " is the delimiter for a 
production, and then we have a noisy expression on the right containing n of 
'(\d+)\s([^,.]+) bags?(.|, )'.

Data structure to express this might be dict[color]:(dict[color]:count ). But 
for the current problem this is not needed, since the question it how many 
distinct tree roots could lead to your color.

So we want to know the relationship in the other direction: given a color, what
might it be contained in?

"""

RE_FIND_COLORS=re.compile('(?:^|\d\s)([\w ]+?)\sbags?')

def parse_rule( rule ):
    """ return (str:color,[str:color]) where the left is the bag and the right
    is the contents.

    >>> parse_rule( "light red bags contain 1 bright white bag, 2 muted yellow bags." )
    ('light red', ['bright white', 'muted yellow'])
    >>> parse_rule( "dark orange bags contain 3 bright white bags, 4 muted yellow bags." )
    ('dark orange', ['bright white', 'muted yellow'])
    >>> parse_rule( "bright white bags contain 1 shiny gold bag." )
    ('bright white', ['shiny gold'])
    >>> parse_rule( "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags." )
    ('muted yellow', ['shiny gold', 'faded blue'])
    >>> parse_rule( "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags." )
    ('shiny gold', ['dark olive', 'vibrant plum'])
    >>> parse_rule( "dark olive bags contain 3 faded blue bags, 4 dotted black bags." )
    ('dark olive', ['faded blue', 'dotted black'])
    >>> parse_rule( "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags." )
    ('vibrant plum', ['faded blue', 'dotted black'])
    >>> parse_rule( "faded blue bags contain no other bags." )
    ('faded blue', [])
    >>> parse_rule( "dotted black bags contain no other bags." )
    ('dotted black', [])
    """
    colors = RE_FIND_COLORS.findall( rule )
    return colors[0],colors[1:]

def parse_rules( rules ):
    """ take list of strings with english rules and return dict of productions
    >>> parse_rules( [ "light red bags contain 1 bright white bag, 2 muted yellow bags.",
    ...     "dark orange bags contain 3 bright white bags, 4 muted yellow bags." ] )
    {'light red': ['bright white', 'muted yellow'], 'dark orange': ['bright white', 'muted yellow']}
    """
    return dict(map(parse_rule, rules))

def decant( dictionary ):
    """ pour one dict-of-lists into another so that the list members are now keys
    >>> decant( { 'a': ['b', 'c'], 'd': ['c', 'f'] } )
    {'b': ['a'], 'c': ['a', 'd'], 'f': ['d']}
    """
    accumulator = collections.defaultdict(list)
    for key, values in dictionary.items():
        for value in values:
            accumulator[value].append(key)
    return dict(accumulator) 

def recurse_sources( visited, paths, bag_color ):
    """ recursively find parents putting them in the set visited.
    >>> bob = set()
    >>> recurse_sources(bob, {'a': ['b', 'c'], 'b':['d'], 'c':['d']}, 'a')
    >>> sorted(bob)
    ['b', 'c', 'd']
    """
    for enclosing_bag in paths.get(bag_color, []):
        if enclosing_bag not in visited:
            visited.add( enclosing_bag )
            recurse_sources( visited, paths, enclosing_bag )
  
def get_list_of_roots(rules, bag_color):
    """ if I want to find a bag of bag_color, what colored bags should I look in?
    >>> get_list_of_roots( EXAMPLE_RULES, 'shiny gold' )
    ['bright white', 'dark orange', 'light red', 'muted yellow']
    """
    paths=decant(parse_rules(rules))
    sources=set()
    recurse_sources( sources, paths, bag_color )
    return sorted(sources)

def day7_1():
    """ How many bags can contain my shiny gold bag?
    >>> day7_1()
    161
    """
    return len(get_list_of_roots(day7input.BAGGAGE_RULES, 'shiny gold'))
