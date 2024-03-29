import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.integrate import odeint
def func(y, x):
    f=np.array([y[1],(x * math.exp(-x) - 4 * y[0] - 8 * y[1]) / 5])
    return f
#графики
y_vector = [1,0]
data1 = np.loadtxt("71.txt")
data2 = np.loadtxt("72.txt")
data3 = np.loadtxt("73.txt")
xg = np.linspace(0,2,2000)
Ode = odeint(func, y_vector, xg)
# plt.plot(xg, Ode[:,0], label = 'Встроенная функция')
# plt.plot(xg, Ode[:,1], label = 'Встроенная функция производная')
# plt.plot(data1[:, 0], data1[:, 1],label='функция от x')
# plt.plot(data2[:, 0], data2[:, 1],'--',label = 'точное решение функции')
# plt.plot(data1[:, 0], data1[:, 2],label='производная функции от x')
# plt.plot(data2[:, 0], data2[:, 2],'--',label='точное решение производной функции')
# plt.plot(data1[:, 1], data1[:, 2],label='фазовый портрет')
# plt.plot(data2[:, 1], data2[:, 2],label='фазовый портрет точного решения')
#plt.plot(data3[:, 0], data3[:, 1],label='разностный график функций')
#plt.plot(data3[:, 0], data3[:, 2],'--',label='разностный график производных функций')
plt.plot(xg[::10],np.abs(data1[:,1]-Ode[::10,0]),label='разностный встроенной функции')
plt.plot(xg[::10],np.abs(data1[:,2]-Ode[::10,1]),'--',label='разностный встроенной производной функции')
plt.legend()
plt.show()
