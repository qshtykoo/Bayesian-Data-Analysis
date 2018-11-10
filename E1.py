from scipy.stats import beta
import matplotlib.pyplot as plt
import numpy as np


x = np.arange(10) / 10
miu = 0.2
var = 0.01
a = miu * ( miu *(1-miu)/var - 1)
b = a * (1 - miu)/miu



plt.subplot(211)
plt.plot(x, beta.pdf(x, a, b), 'r-', lw = 5, alpha = 0.6, label='beta pdf')
plt.subplot(212)
samples = beta.rvs(a, b, size=1000) 
plt.hist(samples)
plt.show()

print("the central 95%-interval of the distribution:", np.percentile(samples, 95))
