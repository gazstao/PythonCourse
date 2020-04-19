import matplotlib.pyplot as plt
import random

vetorx = []
vetory = []

for i in range(10000):
  vetorx.append(random.randint(0,100))
  vetory.append(random.randint(0,100))
plt.scatter(vetorx,vetory, s=3, marker = "*")
#plt.boxplot(vetory)
plt.show()