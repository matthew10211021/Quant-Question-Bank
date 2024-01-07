from random import choice

def sim_bridge_game(no_players, no_steps):
    end = 0  # number of correct tiles that have been discovered up to a certian point
    for i in range(1, no_players+1):
        for j in range(0, no_steps):
            end += 1  # no matter the current player survive or not, he / she helps discover one tile
            if choice([0, 1]) > 0:
                if end >= no_steps: return no_players+1-i  # the current player survive until the end
            else:
                if end >= no_steps: return no_players-i
                break  # the current player is eliminated
    return 0  # no player survives at the end

if __name__ == "__main__":
    rounds = 1000000
    total = 0
    no_players = 16
    no_steps = 18

    for _ in range(rounds): total += sim_bridge_game(no_players, no_steps)
    print(f"Expected number of survivors in a bridge game with {no_steps} steps and {no_players} players is {total / rounds}.")