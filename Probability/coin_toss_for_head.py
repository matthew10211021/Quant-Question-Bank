import numpy as np
from random import choice

def sim_game(A_flips, B_flips, sim_total):
    A_wins = 0

    for _ in range(sim_total):
        A_heads, B_heads = 0, 0

        for _ in range(A_flips):
            if choice(['H', 'T']) == 'H': A_heads += 1

        for _ in range(B_flips):
            if choice(['H', 'T']) == 'H': B_heads += 1

        A_wins += int(A_heads > B_heads)

    return A_wins / sim_total

if __name__ == "__main__":
    A_flips = 20
    B_flips = 21
    total = 100000

    result = sim_game(A_flips, B_flips, total)
    print(f"A wins with probability of {result}.")