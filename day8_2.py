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


