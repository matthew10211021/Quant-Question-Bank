import numpy as np
np.random.seed(69)

def get_prob(hits, attempts, mode):
    hit_rate = hits / attempts
    if mode == "a": return hit_rate
    elif mode == "b": return 1 - hit_rate

def sim_games(mode, n, sim_no):
    results = []

    for _ in range(sim_no):
        hits = 1
        for attempt in range(3, n+1):
            prob = get_prob(hits, attempt-1, mode)
            hits += np.random.binomial(1, prob)
        results.append(hits)

    return results

if __name__ == "__main__":
    n = 10
    sim_no = 10000000
    games_a = sim_games("a", n, sim_no)
    games_b = sim_games("b", n, sim_no)
    ans_a = np.average([x==n-2 for x in games_a])
    ans_b = np.average([x==n-2 for x in games_b])
    print(f"Answer for part a with {n} tosses is {ans_a}")
    print(f"Answer for part b with {n} tosses is {ans_b}")
