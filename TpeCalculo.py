import numpy as np

yi=1
xi=0
xf=1
N=10
h=(xf-xi)/N
y=np.zeros(shape=N+1)

def f(x,y):
    I = 10
    F = I
    C = 0.2
    V = 200
    return (C * I - F/V * y)


def rungeKutta(h, x0, y0):
    x = x0 + h
    k1 = h * f(x0, y0)
    k2 = h * f(x0 + (h/2), y0 + (k1/2))
    k3 = h * f(x0 + (h/2), y0 + (k2/2))
    k4 = h * f(x0 + h, y0 + k3)
    pendiente = (k1 + 2*k2 + 2*k3 + k4)/6
    y = y0 + pendiente

    return y



##Euler
x=xi
y[0] = yi
print(f"En {x}, y = {y[0]}")
for i in range(1,N+1):
    y[i] = y[i-1] + h * f(x,y[i-1])
    x += h
print(f"En {x}, y = {y[i]}")


##Euler Mejorado
print("EULER Mejorado")
x=xi
y[0] = yi
print(f"En {x}, y = {y[0]}")
for i in range(1,N+1):
    yaux = y[i-1] + h * f(x,y[i-1])
    y[i] = y[i-1] + h/2 * (f(x,y[i-1]) + f(x+h,yaux))
    x += h
print(f"En {x}, y = {y[i]}")

## rungeKutta
print("rungeKutta")
x=xi
y[0] = yi
print(f"En {x}, y = {y[0]}")
for i in range(1,N+1):
    y[i] = rungeKutta(h,x,y[i-1])
    x+=h
print(f"En {x}, y = {y[i]}")
