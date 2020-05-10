import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.integrate import odeint
def func(y, x):
    f=np.array([y[1],(x * math.exp(-x) - 4 * y[0] - 8 * y[1]) / 5])
    return f
#точное решение
def tochnoresh(x):
    return 1/2*math.exp(-x)*(2*x+math.exp(x/5)*math.sin(2*x/5)-2*math.exp(x/5)*math.cos(2*x/5)+4)
def proizvodnaya(x):
    return math.exp(-x)*(-x+math.exp(x/5)*math.cos(2*x/5)-1)
#графики
y_vector = [1,1]
data = np.loadtxt("7.txt")
xg = np.linspace(0,2,2000)
yg = [tochnoresh(l) for l in xg]
pryg=[proizvodnaya(l) for l in xg]
Ode = odeint(func, y_vector, xg)
plt.plot(xg, Ode[:,0], label = 'Встроенная функция')
plt.plot(xg, Ode[:,1], label = 'Встроенная функция производная')
plt.plot(data[:, 0], data[:, 1],label='функция от x')
plt.plot(xg,yg,label = 'точное решение функции')
plt.plot(data[:, 0], data[:, 2],label='производная функции от x')
plt.plot(xg,pryg,label='точное решение производной функции')
plt.plot(data[:, 1], data[:, 2],label='фазовый портрет')
plt.legend()
plt.show()