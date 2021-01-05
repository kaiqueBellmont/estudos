import numpy as np
vmysin = np.vectorize(mysin, excluded=['order'])

x = np.linspace(-80, 80, 500)
y2 = vmysin(x, 2)
y10 = vmysin(x, 10)
y100 = vmysin(x, 100)
y1000 = vmysin(x, 1000)
y = np.sin(x)

import matplotlib.pyplot as plt
plt.plot(x, y, label='sin(x)')
plt.plot(x, y2, label='order 2')
plt.plot(x, y10, label='order 10')
plt.plot(x, y100, label='order 100')
plt.plot(x, y1000, label='order 1000')
plt.ylim([-3, 3])
plt.legend()
plt.show()