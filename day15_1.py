""" To play Rambunctious Recitation, we need to keep track of the last position
of each number stated, and hold on to the next number to speak.

"""

class RecitationGame(object):
    def __init__(elf):
        elf._turn = 0
        elf._state = {}

    def take_turn(elf, number):
        elf._turn += 1
        if number in elf._state:
            previous = elf._state[number]
            elf._state[number] = elf._turn
            return elf._turn - previous
        else:
            return 0
    
    def recite(elf, initial_sequence, limit):
        for item in initial_sequence:
            if elf._turn >= limit:
                return next_number
            next_number = elf.take_turn(item) 

        while True:
            if elf._turn >= limit:
                return next_number
            next_number = elf.take_turn(item)

def play_game(initial, limit):
    """
    >>> play_game([0, 3, 6], 10)
    0
    >>> play_game([0, 3, 6], 2019)
    435
    """
    rg = RecitationGame()
    return rg.recite(initial, limit)

