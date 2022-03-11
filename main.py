from stub_data import generate_stub_data

import matplotlib.pyplot as plt

traffic = generate_stub_data(counts=168 * 15, intervals_in_day=15*24)

# %%
plt.title('Model of traffic during a day')
first_day = int(24 * 60 / 15)
x = list(range(0, first_day))
plt.plot(x, traffic[0:first_day])
plt.ylabel('Example of Traffic, GB/s')
plt.xlabel('Interval, 15 minute')
plt.show()

