#!/usr/bin/python

import sys

# n = players
# we want to calculate the total number of combinations (inclusive) of moves for a given number of players

# n=1
# [rock]
# [paper]
# [scissors]

# n = 2
# [rock] [rock]
# [rock] [paper]
# [rock] [scissors]
# [paper] [rock]
# [paper] [paper]
# [paper] [scissors]
# [scissors] [rock]
# [scissors] [paper]
# [scissors] [scissors]

# n = 3
# [rock] [rock] [rock]
# [rock] [rock] [paper]
# [rock] [rock] [scissors]
# [rock] [paper] [rock]
# [rock] [paper] [paper]
# [rock] [paper] [scissors]
# [rock] [scissors] [rock]


# [paper] [rock]
# [paper] [paper]
# [paper] [scissors]
# [scissors] [rock]
# [scissors] [paper]
# [scissors] [scissors]

moves = [["rock"], ["paper"], ["scissors"]]

# plays = [[length of n]... all permutations of r/p/s]
def rock_paper_scissors(n):
    plays = list()

    def play_combos(n, plays):
        temp = list()
        if n <= 0:
            return [[]]
        elif len(plays) < 1:
            temp.append(moves[0])
            temp.append(moves[1])
            temp.append(moves[2])
        else:
            for move in moves:
                for play in plays:
                    temp.append(move + play)
        if n == 1:
            return temp

        return play_combos(n - 1, temp)

    return play_combos(n, plays)


rock_paper_scissors(4)
# if __name__ == "__main__":
#     if len(sys.argv) > 1:
#         num_plays = int(sys.argv[1])
#         print(rock_paper_scissors(num_plays))
#     else:
#         print("Usage: rps.py [num_plays]")

