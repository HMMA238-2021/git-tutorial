import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)

# Gaussian
mu, sigma = 100, 15
x_gaussian = mu + sigma * np.random.randn(10000)

np.savetxt('file_data_gaussian.csv', x_gaussian, delimiter=',')

# Non Gaussian
mu_2, sigma_2 = 100, 5
x_chisq = mu_2 + sigma_2 * (np.random.randn(10,10000) ** 2).sum(0)

np.savetxt('file_data_chisq.csv', x_chisq, delimiter=',')

