import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = 3 * x + 2

plt.plot(x, y, label='y = 3x + 2', color='blue')

plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.title('Line Chart of y = 3x + 2')
plt.legend()

plt.grid()
plt.show()
