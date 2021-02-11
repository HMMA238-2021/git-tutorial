import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)

mu, sigma = 100, 5
x_chisq = mu + sigma * (np.random.randn(10,10000) ** 2).sum(0)

np.savetxt('file_data_chisq.csv', x_chisq, delimiter=',')
