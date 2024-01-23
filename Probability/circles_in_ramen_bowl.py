import random
import numpy as np
random.seed(42)

def initialize_bowl(count):
    bowl = {}
    bowl["circles"] = {}
    bowl["segments"] = {i: 1 for i in range(1, count+1)}
    return bowl

def select_noodles(bowl):
    noodle_ends = list(bowl["segments"].keys()) * 2
    selected_ends = random.sample(noodle_ends, 2)
    return selected_ends

def connect_noodles(bowl, ends):
    if ends[0] == ends[1]:
        bowl["circles"][ends[0]] = bowl["segments"][ends[0]]
        del  bowl["segments"][ends[0]]
    else:
        bowl["segments"][f"{ends[0]}_{ends[1]}"] = bowl["segments"][ends[0]] + bowl["segments"][ends[1]]
        del bowl["segments"][ends[0]], bowl["segments"][ends[1]]
    
    return bowl

def sim_game(count):
    bowl = initialize_bowl(count)
    for i in range(count):
        ends = select_noodles(bowl)
        bowl = connect_noodles(bowl, ends)

    return (len(bowl["circles"].keys()), max(bowl["circles"].values()))

if __name__ == "__main__":
    result = np.mean([sim_game(100) for x in range(10**5)], axis=0)
    print(f"Expected number of circles is {result[0]}")
    print(f"Expected maximum length of circles is {result[1]}")