from random import shuffle
import numpy as np

def expected_draws_to_get_ace(sim_no):
    cards = ["A" if i%13==0 else "NA" for i in range(52)]

    cards_drawn = []
    for _ in range(sim_no):
        shuffled_cards = shuffle(cards)
        for i in range(52):
            if cards[i] == "A":
                cards_drawn.append(i+1)
                break

    return np.mean(cards_drawn)

if __name__ == "__main__":
    sim_no = 1000000
    result = expected_draws_to_get_ace(sim_no)
    print(f"Expected number of cards drawn to get an ACE is {result}.")