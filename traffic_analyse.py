import math
import random as rand
import numpy as np


class TrafficDeviationDto:

    def __init__(self, is_normal: bool, deviation: float) -> None:
        self.is_normal = is_normal
        self.deviation = deviation


class TrafficAnalyzer:

    def __init__(self):
        self.means = None
        self.stds = None

    def fit(self, data: [], intervals_in_day: int):
        np_array = np.array(data).reshape((-1, intervals_in_day))
        print(f'Teaching analyzer on {np_array.shape[0]} samples per day'
              f' for {np_array.shape[1]} days')

        means = np.mean(np_array, axis=0)
        stds = np.std(np_array, axis=0)
        print(f'{means.shape} means, {stds.shape} std taken')

        self.means = means
        self.stds = stds

    def is_normal(self, traffic: float, interval: int) -> TrafficDeviationDto:
        m = self.means[interval]
        q = self.stds[interval]
        is_normal = self._is_normal_criteria(traffic, m, q)
        deviation = traffic / m
        return TrafficDeviationDto(is_normal=is_normal, deviation=deviation)

    def _is_normal_criteria(self, value: float, m: float, q: float):
        sigmas = 3
        return abs(value - m) < q * sigmas
