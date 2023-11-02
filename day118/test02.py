import matplotlib.pyplot as plt
import numpy as np

dice = np.random.choice(6, 100000, p=[0.1, 0.1, 0.1, 0.1, 0.1, 0.5])

plt.hist(dice, bins=6)
plt.show()
