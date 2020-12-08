EXAMPLE_PROGRAM=[
    "nop +0",
    "acc +1",
    "jmp +4",
    "acc +3",
    "jmp -3",
    "acc -99",
    "acc +1",
    "jmp -4",
    "acc +6" ]

EXAMPLE_FIXED=[
    "nop +0",
    "acc +1",
    "jmp +4",
    "acc +3",
    "jmp -3",
    "acc -99",
    "acc +1",
    "nop -4",
    "acc +6" ]


def parse_instruction( instruction ):
    """ split an instruction line into its operation and argument
    >>> parse_instruction('nop +0')
    ('nop', 0)
    >>> parse_instruction('acc -99')
    ('acc', -99)
    """
    op,arg = instruction.split(' ')
    return op, int(arg)

def read_program( iterable ):
    return list(map(parse_instruction,iterable))

STATUS_OK=0
STATUS_LOOP=1
def catch_loop( program ):
    """ what was the value of the accumulator when the program revisited an 
    instruction?
        
    Function is a naive implementation of the computer, that keeps a checklist
    of program-counter values. If a program-counter value is repeated, then it
    stops, returning the value in the accumulator.

    >>> catch_loop(read_program(EXAMPLE_PROGRAM))
    (1, 5)
    >>> catch_loop(read_program(EXAMPLE_FIXED))
    (0, 8)
    """
    visited = set()
    program_counter=0
    accumulator=0
    out_of_bounds=len(program)
    while program_counter<out_of_bounds and program_counter not in visited:
        step=1 # what to add to program_counter next
        op, arg = program[program_counter]

        if op == 'acc':
            accumulator += arg
        elif op == 'jmp':
            step = arg

        visited.add(program_counter)
        program_counter+=step

    return STATUS_OK if program_counter>=out_of_bounds else STATUS_LOOP, accumulator

def day8_1():
    """
    >>> day8_1()
    2080
    """
    with open('day8input.txt','r') as fp:
        return catch_loop(read_program(fp))[1]

