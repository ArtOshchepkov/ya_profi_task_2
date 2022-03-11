from stub_data import generate_stub_data

import matplotlib.pyplot as plt

from traffic_analyse import TrafficAnalyzer

INTERVALS_IN_DAY = 15 * 24

traffic = generate_stub_data(counts=168 * 15, intervals_in_day=INTERVALS_IN_DAY)

# %%
plt.title('Model of traffic during a day')
first_day = int(24 * 60 / 15)
x = list(range(0, first_day))
plt.plot(x, traffic[0:first_day])
plt.ylabel('Example of Traffic, GB/s')
plt.xlabel('Interval, 15 minute')
plt.show()


# %%
traffic_analyzer = TrafficAnalyzer()
traffic_analyzer.fit(traffic, INTERVALS_IN_DAY)
