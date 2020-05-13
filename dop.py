import numpy as np
import matplotlib.pyplot as plt
import math
def f(x,y):
    return [y[1], 1/5*(x*math.exp(-x)-4*y[0]-8*y[1])]
def F(f,y0,a,b,e):
    h=0.001
    kq=(b-a)/h
    kq=math.trunc(kq)
    print('Взять число точек на графике: ',kq)
    n=len(y0)
    print('Порядок дифференциального уравнения: ', n)
    x=[a+h*l for l in range (0,kq)]
    y=np.zeros((n,kq))
    for i in range (0,n):
        y[i,0]=y0[i]
    
    #находим y1 2-кратным методом Хойна
    k1=np.zeros(n)
    k2=np.zeros(n)

    
    k1=f(a,[y[i,0] for i in range(0,n)])
    k2=f(a+h/2,[y[i,0]+h/2*k1[i] for i in range(0,n)])
   
    for i in range (0,n):
        y[i,1]=y[i,0]+h/2*(k1[i]+k2[i])
    
    #неявный метод Адамса при k=1 
    yst=90*np.ones((n,kq))
    ynov=np.ones((n,kq))
    for i in range (0,n):
        yst[i,0]=y0[i]
        ynov[i,0]=y0[i]
        yst[i,1]=y[i,1]
        ynov[i,1]=y[i,1]
        
    it=0
    while math.fabs((ynov[0,-1]-yst[0,-1])/(ynov[0,-1]))>e:
        it+=1
        for j in range(2,kq):
            for i in range (0,n):
                yst[i,j]=ynov[i,j]
            for i in range (0,n):
                ynov[i,j]=ynov[i,j-1]+h/12*(5*f(x[j],ynov[:,j])[i]+8*f(x[j-1],ynov[:,j-1])[i]-f(x[j-2],ynov[:,j-2])[i])
    print('Число итераций для достижения заданной точности: ', it)
    print('Решение: ', ynov[0,:])
    print('Производная: ', ynov[1,:])
    return ynov[0,:],ynov[1,:]
#точное решение
def tochnoresh(x):
    return 1/2*math.exp(-x)*(2*x+math.exp(x/5)*math.sin(2*x/5)-2*math.exp(x/5)*math.cos(2*x/5)+4)
def proizvodnaya(x):
    return math.exp(-x)*(-x+math.exp(x/5)*math.cos(2*x/5)-1)
#Метод Хойна 2-кратный
def runge_kutt(f,y0,a,b,e):
    h=0.001
    kq=(b-a)/h
    kq=math.trunc(kq)
    n=len(y0)
    x=[a+h*l for l in range (0,kq)]
    yrk=np.zeros((n,kq))
    k11=np.zeros(n); k22=np.zeros(n)
    for i in range (0,n):  
        yrk[i,0]=y0[i]
    for j in range (1,kq):
        k11=np.zeros(n); k22=np.zeros(n)
        k11=f(x[j-1],[yrk[i,j-1] for i in range(0,n)])
        k22=f(x[j-1]+h/2,[yrk[i,j-1]+h/2*k11[i] for i in range(0,n)])
      
        for i in range (0,n):
            yrk[i,j]=yrk[i,j-1]+h/6*(k11[i]+2*k22[i])
    return yrk[0,:], yrk[1,:]
#графики
xg = np.linspace(0,2,2000)
yg = [tochnoresh(l) for l in xg]
pryg=[proizvodnaya(l) for l in xg]
yrkg,pryrkg=runge_kutt(f,[1,0],0,2,0.01)
yfazpl,pryfazpl=F(f,[1,0],0,2,0.01)
plt.plot(xg,yrkg,label='график функции')
plt.plot(xg,yg,label = 'график функции точного решения')
plt.plot(xg,pryrkg,label='график производной функции')
plt.plot(xg,pryg,label='график производной функции точного решения')
plt.plot(yfazpl,pryfazpl, label='фазовая траектория')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.show
