import numpy as np

def cal_prob_normal(sim_no):
    x = np.random.normal(loc=0, scale=1, size=sim_no)
    y = 4 * np.random.normal(loc=0, scale=1, size=sim_no)

    return np.mean(x>y)

def cal_prob_uniform(sim_no):
    x = np.random.uniform(low=0, high=1, size=sim_no)
    y = 4 * np.random.uniform(low=0, high=1, size=sim_no)

    return np.mean(x>y)

if __name__ == "__main__":
    sim_no = 1000000
    ans_a = cal_prob_normal(sim_no)
    ans_b = cal_prob_uniform(sim_no)

    print(f"Answer for part (a) is {ans_a}; Answer for part (b) is {ans_b}.")
