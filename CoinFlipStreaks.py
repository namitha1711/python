import random

def generate_coin_flips(n):
    return [random.choice(['H', 'T']) for _ in range(n)]

def count_streaks(flips, streak_length):
    streak_count = 0
    for i in range(len(flips) - streak_length + 1):
        if len(set(flips[i:i + streak_length])) == 1:
            streak_count += 1
    return streak_count

def experiment(num_experiments, num_flips, streak_length):
    streaks = 0
    for _ in range(num_experiments):
        flips = generate_coin_flips(num_flips)
        streaks += count_streaks(flips, streak_length)
    return streaks / num_experiments

def main():
    num_experiments = 10000
    num_flips = 100
    streak_length = 6
    print(experiment(num_experiments, num_flips, streak_length))
main()
