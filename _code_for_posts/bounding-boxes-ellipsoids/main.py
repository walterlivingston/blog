import numpy as np
import matplotlib.pyplot as plt

n = 100
mean = [5, 10]
std_dev = [1.0, 3.0]

points = np.random.normal(loc=mean, scale=std_dev, size=(n, 2))

plt.figure()
plt.scatter(points[:, 0], points[:, 1])
plt.title("Random (x, y) Points with Mean and Std Dev")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.axis('equal')
plt.show()