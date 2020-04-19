import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 6.3, 100)

plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))
plt.plot(x, x*0)

plt.show()