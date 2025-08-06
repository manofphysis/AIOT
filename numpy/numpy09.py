import matplotlib.pyplot as plt
import numpy as np

numbers = np.random.normal(size=10000)
plt.hist(numbers, bins=50, density=True)
plt.title('Histogram of Normally Distributed Random Numbers')   
plt.xlabel('Value')
plt.ylabel('Density')   
plt.show()
