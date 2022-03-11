import math
import random as rand

rand.seed(42)


def generate_interval_sin(interval, intervals_in_day, q=3_000, around=5_000):
    x = interval / intervals_in_day * 2 * 3.1415
    return (math.sin(x) + 1.0) * around + (rand.random()) * q


def generate_stub_data(points: int, intervals_in_day: int):
    print(f'Generate {points} points with {intervals_in_day} intervals per day')
    return list(map(lambda i: generate_interval_sin(i, intervals_in_day), range(1, points + 1)))
