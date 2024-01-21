import numpy as np

p1, p2 = 0.42, 0.5
n_min = 418
p_mid = 0.459741
threshold = n_min * p_mid

correct_guess = []
for _ in range(1000000):
    coin = np.random.choice(["Fair", "Unfair"])
    p = p1 if coin == "Unfair" else p2

    # simulate throws
    heads = np.random.binomial(n_min, p)
    guess = "Unfair" if heads <= threshold else "Fair"

    correct_guess.append(guess==coin)

print(f"Portion of correct guess is {np.mean(correct_guess)}")