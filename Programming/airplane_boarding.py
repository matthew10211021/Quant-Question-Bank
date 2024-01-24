import random
from collections import Counter

random.seed(42)

no_seats = 20
no_psg_list = [20, 30, 40]
sim_no = 1000000

def reservoir_sampling(no_seats, no_passengers):
    seat_psg_map = {}
    for i in range(1, no_passengers+1):
        if i <= no_seats:
            seat_psg_map[i] = i
        else:
            r = random.randint(1, i)
            if r <= no_seats:
                seat_psg_map[r] = i

    return seat_psg_map

relative_freq_table = {}

for psg in no_psg_list:
    relative_freq_table[psg] = {}

    boarded_psgs = []
    for i in range(sim_no):
        boarded_psgs += list(reservoir_sampling(no_seats, psg).values())

    counter = Counter(boarded_psgs)
    total_count = sum(counter.values())

    for key, value in counter.items():
        relative_freq_table[psg][key] = value / total_count

print(relative_freq_table)