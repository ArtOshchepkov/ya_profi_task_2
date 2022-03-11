import numpy as np

from stub_data import generate_stub_data

import matplotlib.pyplot as plt

from traffic_analyse import TrafficAnalyzer, TrafficDeviationDto

INTERVALS_IN_DAY = int(24 * (60 / 15))
DAYS = 50
POINTS = DAYS * INTERVALS_IN_DAY

print(f'Generate some stub data considering {INTERVALS_IN_DAY} intervals per day')
traffic = generate_stub_data(points=POINTS, intervals_in_day=INTERVALS_IN_DAY)
plt.plot(traffic)
plt.show()

# %%
plt.title('Model of traffic during a day')
x = list(range(0, INTERVALS_IN_DAY))
# plt.plot(x, traffic[0:INTERVALS_IN_DAY])
plt.ylabel('Example of Traffic, GB/s')
plt.xlabel('Interval, 15 minute')
# plt.show()

# %%
traffic_analyzer = TrafficAnalyzer()
traffic_analyzer.fit(traffic, INTERVALS_IN_DAY)


def test_analyzer(traffic_data: [], intervals: [], analyzer: TrafficAnalyzer, original_data):
    def to_colors(deviation: TrafficDeviationDto):
        return 'green' if deviation.is_normal else 'red'

    def to_deviation(point: []):
        return analyzer.is_normal(point[0], point[1])

    colors = list(map(to_colors, map(to_deviation, list(zip(traffic_data, intervals)))))
    np_array = np.array(original_data).reshape((-1, INTERVALS_IN_DAY))
    print(np_array.shape)
    average_traffic = np.mean(np_array, axis=0)
    print(average_traffic.shape)
    x = list(range(0, INTERVALS_IN_DAY))

    plt.grid()
    plt.plot(average_traffic)
    # plt.ylim((4800, 5200))
    plt.title('Traffic, Green - normal, red - abnormal')
    plt.ylabel('Traffic, GB/s')
    plt.xlabel('Interval, 15 minute')
    plt.scatter(x=intervals, y=traffic_data, color=colors)
    plt.show()


traffic_test = [4000, 8000, 6000, 5000, 11000, 11_000, 13000, 4000, 8000, 11_000, 13_000, 10_000, 13_000, 6000, 4000, 3500, 6000, 8000, 3500, 5000, 3500, 7000]
intervals_test = [0, 0, 0, 0, 0, 20, 20, 20, 20, 20, 20, 40, 40, 40, 40, 40, 40, 40, 40, 60, 60, 60]
test_analyzer(traffic_test, intervals_test, traffic_analyzer, original_data=traffic)
