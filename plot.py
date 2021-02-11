import numpy as np
import matplotlib.pyplot as plt

# Data are loaded from a file
x_gaussian = np.loadtxt('file_data_gaussian.csv')

# the histogram of the data
n, bins, patches = plt.hist(x_gaussian, 50, density=True, facecolor='r', alpha=0.74)

plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$ This one is Gaussian !')
plt.xlim(40, 160)
plt.ylim(0, 0.03)
plt.grid(True)
plt.show()
