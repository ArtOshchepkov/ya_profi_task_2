import math
import random as rand

rand.seed(42)


def generate_interval_sin(interval, intervals_in_day, q=1_000, around=5_000):
    x = interval / intervals_in_day * 3.1415 * 8 - 3.1415 / 4
    return (math.sin(x) + 0.5) * around + (rand.random() - 0.5) * 2 * q


def generate_stub_data(counts=168 * 15, intervals_in_day=24 * 60 / 15):
    return list(map(lambda i: generate_interval_sin(i, intervals_in_day), range(0, counts)))
