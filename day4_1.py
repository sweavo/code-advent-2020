from day4input import DAY4_INPUT

DEMO_INPUT=[ 
    "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd",
    "byr:1937 iyr:2017 cid:147 hgt:183cm",
    "",
    "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884",
    "hcl:#cfa07d byr:1929",
    "",
    "hcl:#ae17e1 iyr:2013",
    "eyr:2024",
    "ecl:brn pid:760753108 byr:1931",
    "hgt:179cm",
    "",
    "hcl:#cfa07d eyr:2025 pid:166559648",
    "iyr:2011 ecl:brn hgt:59in" ]

MANDATORY_FIELDS= [ 'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid' ]

def yield_records( input_lines ):
    """
        >>> len(list( yield_records( DEMO_INPUT ) ) )
        4
        >>> list( yield_records( DEMO_INPUT ) )[3]
        'hcl:#cfa07d eyr:2025 pid:166559648 iyr:2011 ecl:brn hgt:59in'
        """
    buffer = ""
    for line in input_lines:
        if "" == line:
            yield buffer[1:]
            buffer=""
        else:
            buffer += (" " + line)
    if buffer != "":
        yield buffer[1:]

def parse_record( record_string ):
    """
        >>> parse_record( 'ecl:brn pid:760753108' )
        {'ecl': 'brn', 'pid': '760753108'}
        """
    return dict( map( lambda r: r.split(':'), record_string.split(' ') ) )

def missing_fields( MANDATORY_FIELDS, record ):
    """
        >>> test_data = list(map(parse_record, yield_records( DEMO_INPUT) ) )
        >>> missing_fields( MANDATORY_FIELDS, test_data[0] )
        []
        >>> missing_fields( MANDATORY_FIELDS, test_data[2] )
        []
        >>> missing_fields( MANDATORY_FIELDS, test_data[3] )
        ['byr']
        """
    return list( filter( lambda x: x not in record, MANDATORY_FIELDS ) ) 

def is_valid( record ):
    """ READS GLOBAL so that it can be treated as a lambda
        >>> test_data = list(map(parse_record, yield_records( DEMO_INPUT) ) )
        >>> is_valid( test_data[0] )
        True
        >>> is_valid( test_data[3] )
        False
        """
    return [] == missing_fields( MANDATORY_FIELDS,  record )

def count_valid( records ):
    """ READS GLOBAL in is_valid
        >>> test_iterator = map(parse_record, yield_records( DEMO_INPUT) )
        >>> count_valid( test_iterator )
        2
        """
    return len( list( filter( is_valid, records ) ) )

def day4_1():
    """
        >>> day4_1()
        216
        """
    return count_valid( map( parse_record, yield_records( DAY4_INPUT ) ) )