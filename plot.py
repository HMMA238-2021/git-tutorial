import numpy as np
import matplotlib.pyplot as plt


# Data are loaded from a file
x_gaussian = np.loadtxt('file_data_gaussian.csv')
x_chisq = np.loadtxt('file_data_chisq.csv')

# the histograms of the data
n, bins, patches = plt.hist(x_gaussian, 50, density=True, facecolor='r', alpha=0.74) # Gaussian
n, bins, patches = plt.hist(x_chisq, 50, density=True, facecolor='k', alpha=0.25) # Chi-squared


plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')

plt.text(60, .025, r'$\mu=100,\ \sigma=15\quad $ This one is Gaussian !')
plt.text(95, .010, r'$\mu=100,\ \sigma=5\quad $ but this one is a Chi-squared')

plt.xlim(40, 250)
plt.ylim(0, 0.03)
plt.grid(True)
plt.show()
