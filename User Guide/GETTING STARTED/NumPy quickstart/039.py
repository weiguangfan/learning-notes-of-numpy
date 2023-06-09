import numpy as np
import matplotlib.pyplot as plt
rg = np.random.default_rng(1)
print(rg)
mu, sigma = 2, 0.5
v = rg.normal(mu, sigma, 10000)
print(v)
# plt.hist(v, bins=50, density=True)
# plt.show()

(n, bins) = np.histogram(v, bins=50, density=True)
print(n)
print(bins)
plt.plot(.5 * (bins[1:] + bins[:-1]), n)
plt.show()