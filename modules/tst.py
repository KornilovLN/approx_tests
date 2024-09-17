#!/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline

x = np.linspace(0, 10, 50)
#y = np.sin(2*x)*np.exp(-x**2) +0.1*np.random.randn(50)
y = np.exp(-x**2) + 0.05 * np.random.randn(50)

# ‘s’ — определяет количество узлов, указывая условие сглаживания.
# 'k' — определяет степень полинома, используемого для сглаживания.
spl = UnivariateSpline(x,y,k=3,s=7)
xs = np.linspace(0, 10, 100)

plt.figure(figsize=(12, 6))
plt.plot(x,y,'ro',ms=5)

plt.plot(xs, spl(xs), 'g', lw=3)

plt.savefig('tst_spline_cube.png')
plt.show()

'''
cubic = interpolate.interp1d(x_data, y_data, kind="cubic")
y_cubic = cubic(xh)

fig, ax = plt.subplots(figsize=(10, 8), layout="tight")
ax.plot(xh, y_cubic, label="Кубический сплайн")
plot_problem(ax, x_data, y_data)
ax.legend()
ax.set_title("Интерполяция кубическим сплайном")
'''