import random
import numpy as np

def sim_game():
    a1 = random.uniform(0, 1)
    a2 = random.uniform(0, 1)

    answer = np.sign(a2-a1)
    guess = np.sign(0.5-a1)

    result = int(answer == guess)
    return result

if __name__ == "__main__":
    sim_no = 1000000
    wins = [sim_game() for _ in range(sim_no)]
    print(f"Winning probability is {np.mean(wins)}")