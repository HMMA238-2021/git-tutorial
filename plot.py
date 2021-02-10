import numpy as np
import matplotlib.pyplot as plt

# Data are loaded from a file
gaussian = np.loadtxt('file_data_gaussian.csv')
chisqrd = np.loadtxt('file_data_chisqrd.csv')
# the histogram of the data
n, bins, patches = plt.hist(gaussian, 50, density=True, facecolor='r', alpha=0.74)
n, bins, patches = plt.hist(chisqrd, 50, density=True, facecolor='b', alpha=0.25)

plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.text(80, .020, r'$\mu=100,\ \sigma=5$')
plt.xlim(40, 250)
plt.ylim(0, 0.03)
plt.grid(True)
plt.show()
