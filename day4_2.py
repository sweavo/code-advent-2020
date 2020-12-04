import re

import day4_1

def in_closed_range( lower, value, upper ):
    """
        >>> in_closed_range( 1, 0 ,3 )
        False
        >>> in_closed_range( 1, 1 ,3 )
        True
        >>> in_closed_range( 1, 2 ,3 )
        True
        >>> in_closed_range( 1, 3 ,3 )
        True
        >>> in_closed_range( 1, 4 ,3 )
        False
        """
    return lower <= value and value <= upper
    
def validate_byr( byr ):
    return in_closed_range( 1920, int(byr), 2002 )

def validate_iyr( iyr ):
    return in_closed_range( 2010, int(iyr), 2020 )

def validate_eyr( eyr ):
    return in_closed_range( 2020, int(eyr), 2030 )
  
RE_HGT_SPLIT=re.compile('^(\d+)(in|cm)$')
def validate_hgt( hgt ):
    """
        >>> validate_hgt('in')
        False
        >>> validate_hgt('60in')
        True
        >>> validate_hgt('190cm')
        True
        >>> validate_hgt('190in')
        False
        >>> validate_hgt('190')
        False
        """
    m = RE_HGT_SPLIT.match(hgt)
    if m is None:
        return False
    
    value, unit = m.groups()
    if unit == 'in':
        return in_closed_range( 59, int(value), 76 )
    elif unit == 'cm':
        return in_closed_range( 150, int(value), 193 )
    else:
        return False

RE_HCL_VALID = re.compile('^#[0-fa-f]{6}$')
def validate_hcl( hcl ):
    """
        >>> validate_hcl( '#123abc' )
        True
        >>> validate_hcl( '#123abz' )
        False
        >>> validate_hcl( '123abc' )
        False
        >>> validate_hcl( '#123ab' )
        False
        >>> validate_hcl( '#123abcd' )
        False
        """
    return RE_HCL_VALID.match(hcl) is not None

def validate_ecl( ecl ):
    return ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

RE_PID_VALID = re.compile('^\d{9}$')
def validate_pid( pid ):
    return RE_PID_VALID.match(pid) is not None

def validate_cid( cid ):
    return True

VALIDATION_TABLE={
    'byr': validate_byr,
    'iyr': validate_iyr,
    'eyr': validate_eyr,
    'hgt': validate_hgt,
    'hcl': validate_hcl,
    'ecl': validate_ecl,
    'pid': validate_pid,
    'cid': validate_cid
    }

def validate_field( key, record ):
    """ pass the value of the field to the validation function for the field """
    return VALIDATION_TABLE[key](record[key])

def validate_record( record ):
    """
        >>> validate_record( day4_1.parse_record( 'eyr:1972 cid:100 hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926' ) )
        False
        >>> validate_record( day4_1.parse_record( 'pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980 hcl:#623a2f' ) )
        True
        """
    return all( [ field in record 
              and validate_field( field, record )
              for field in day4_1.MANDATORY_FIELDS ] )

def day4_2():
    """
        >>> day4_2()
        150
        """
    return day4_1.count_valid( validate_record, day4_1.yield_live_records() )

