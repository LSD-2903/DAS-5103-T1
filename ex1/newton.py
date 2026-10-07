from math import sin, pi, cos
from matplotlib import pyplot as plt
def f(x):
    return 100**2/9.8*(sin(x) + 0.5*sin(2*x)) - 1000

def c(x):
    return -1/(100**2/9.8*(cos(x) + cos(2*x)))

def g(x):
    return x + c(x)*f(x)

def newton(x0, e, n):
    k = 0
    array = []
    while True:
        k += 1
        if k > n:
            print(f"Não foi possível encontrar raíz dentro de {k}  iterações")
            return
        
        x1 = g(x0)
        array.append((x1, f(x1)))

        if abs(x1 - x0) <= e:
            return array
        x0 = x1

x0 = 0.8
e = 10**-5
n = 100

array = newton(x0, e, n)

print(f"O chute inicial {x0} convergiu em {len(array)} iterações para o valor {array[-1][0]}")

fig, ax = plt.subplots(2, 1)

ax[0].plot([i+1 for i in range(len(array))], [tupla[0] for tupla in array], marker = 'o') # 0 para x e 1 para fx
ax[0].set_title("θ")

ax[1].plot([i+1 for i in range(len(array))], [tupla[1] for tupla in array], marker = 'o') # 0 para x e 1 para fx
ax[1].set_title("f(θ)")
plt.show()