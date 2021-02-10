import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)

mu, sigma = 100, 15

x_gaussian = mu + sigma * np.random.randn(10000)

mu, sigma = 100, 5
x_chisqrd = mu + sigma * (np.random.randn(10,10000) ** 2).sum(0)



np.savetxt('file_data_gaussian.csv', x_gaussian, delimiter=',')
np.savetxt('file_data_chisqrd.csv', x_chisqrd, delimiter=',')