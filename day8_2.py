import day8_1

""" puzzle is to take the broken program of day8input.txt and change exactly 
one jmp to a nop such that the program terminates. Verification is by posting
the value of the accumulator when the program does terminate.

Approach: 

load the program, enumerate its jmps, and try executing it with the jmp 
substituted until it terminates correctly.

Updates needed on part 1's computer:

1) terminate on reaching the end
2) indicate whether it was a termination or a loop that stopped the evaluation
"""

def knock_out_jumps( program ):
    """ given a prepared program, replace jmp with nop one at a time.

    yields the resulting programs.

    >>> ip = [('acc', 1), ('jmp', 4), ('jmp', -3),('acc',-3)]
    >>> iterator = knock_out_jumps(ip)
    >>> iterator.__next__()
    [('acc', 1), ('nop', 4), ('jmp', -3), ('acc', -3)]
    >>> iterator.__next__()
    [('acc', 1), ('jmp', 4), ('nop', -3), ('acc', -3)]
    >>> len(list(knock_out_jumps(day8_1.read_program(day8_1.EXAMPLE_PROGRAM))))
    3
    """
    input_program = list(program) # insurance against being given an iterator

    for index, instruction in enumerate(input_program):
        op, arg = instruction
        if op == 'jmp':
            yield input_program[:index] + [( 'nop', arg )] + input_program[index+1:]

def find_passing_program(programs):
    """ return the accumulator resulting from the first program in programs 
    that terminates.

    >>> find_passing_program(map(day8_1.read_program,
    ...                         [ day8_1.EXAMPLE_PROGRAM,
    ...                           day8_1.EXAMPLE_FIXED]))
    8
    >>> find_passing_program(
    ...     knock_out_jumps(
    ...         day8_1.read_program( day8_1.EXAMPLE_PROGRAM ) ) )
    8
    """
    for program in programs:
        status, accumulator = day8_1.catch_loop( program )
        if status == day8_1.STATUS_OK:
            return accumulator

def day8_2():
    """
    >>> day8_2()
    2477
    """
    with open('day8input.txt','r') as fp:
        broken_program=day8_1.read_program( fp )
    return find_passing_program( knock_out_jumps( broken_program ) )

