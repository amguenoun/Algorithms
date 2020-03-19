#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    poss = []
    game = ['rock', 'paper', 'scissors']

    def find_hands(n, game_list):
        if n == 0:
            poss.append(game_list)
            return
        else:
            for play in game:
                find_hands(n-1, game_list + [play])

    find_hands(n, [])

    return poss


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
