from collections import Counter
from random import choice

def airplane_boarding(passengers, sim_no):
    results = []
    for _ in range(sim_no):
        free_seats = set(range(1, passengers+1))
        for i in range(1, passengers):
            if i == 1 or i not in free_seats: free_seats -= {choice(list(free_seats))}
            else: free_seats -= {i}
        
        results.append(list(free_seats)[0])

    return results

if __name__ == "__main__":
    passengers = 100
    sim_no = 1000000

    result = airplane_boarding(passengers, sim_no)
    freq = Counter(result)
    print(f"Probability for the last passenger to get his / her own seat is {freq[passengers]/sim_no}")