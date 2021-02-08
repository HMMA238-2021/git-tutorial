import numpy as np
import matplotlib.pyplot as plt

# Data are loaded from a file
x = np.loadtxt('file_data.csv')

# the histogram of the data
n, bins, patches = plt.hist(x, 50, density=True, facecolor='#229C6C', alpha=0.83)

plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.xlim(40, 160)
plt.ylim(0, 0.03)
plt.grid(True)
plt.show()
