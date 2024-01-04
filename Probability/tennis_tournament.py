import random
from collections import defaultdict
import numpy as np

def sim_tournament(required_game=2):
    players = set(['A', 'B', 'C'])
    waiting_player = set('C')
    prev_winner = np.nan
    count_wins = 0

    while count_wins != required_game:
        match_players = players - waiting_player  # set difference
        match_winner = random.choice(list(match_players))
        waiting_player = match_players - set(match_winner)

        if match_winner == prev_winner: count_wins += 1
        else: count_wins = 1

        prev_winner = match_winner

    return match_winner

if __name__ == "__main__":
    wins = defaultdict(int)
    no_of_games = 9999
    for required_game in range(2, 11):
        for _ in range(no_of_games):
            win = sim_tournament(required_game)
            wins[win] += 1

        print(f"probability of winning for C with {required_game} consecutive wins required: {wins['C']/no_of_games}")
        wins = defaultdict(int)