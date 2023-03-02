import numpy as np
import matplotlib.pyplot as plt

n = 10000
x = np.cumsum(np.random.randn(n))
y = np.cumsum(np.random.randn(n))
plt.plot(x,y)

