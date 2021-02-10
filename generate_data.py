import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)

<<<<<<< HEAD
mu, sigma = 100, 15
x_gaussian = mu + sigma * np.random.randn(10000)
=======
mu, sigma = 100, 5
x = mu + sigma * (np.random.randn(10,10000) ** 2).sum(0)
>>>>>>> 47fb5f2 (Data generation is no longer Gaussian!)

np.savetxt('file_data.csv', x_gaussian, delimiter=',')
