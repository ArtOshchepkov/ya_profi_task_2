import math
import random as rand
import numpy as np


class TrafficAnalyzer:

    def __init__(self):
        self.means = None
        self.stds = None

    def fit(self, data, indexes_in_day):
        np_array = np.array(data).reshape((indexes_in_day, -1))
        print(f'Teaching analyzer on {np_array.shape[0]} samples per day'
              f' for {np_array.shape[1]} days')

        means = np.mean(np_array, axis=1)
        stds = np.std(np_array, axis=1)
        print(f'{means.shape[0]} means, std taked')

        self.means = means
        self.stds = stds
