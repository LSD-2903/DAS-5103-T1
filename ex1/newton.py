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
    while k < n:
        k += 1
        
        x1 = g(x0)
        array.append((x1, f(x1)))

        if abs(f(x1)) <= e:
            return array
        x0 = x1
    return

x0 = 0.8
e = 10**-5
n = 100

array = newton(x0, e, n)
if array:
    print(f"O valor inicial {x0} convergiu em {len(array)} iterações para {array[-1][0]}")

    fig, ax = plt.subplots(2, 1)
    
    ax[0].plot([i+1 for i in range(len(array))], [tupla[0] for tupla in array], marker = 'o')
    ax[0].set_title("θ")

    ax[1].plot([i+1 for i in range(len(array))], [tupla[1] for tupla in array], marker = 'o')
    ax[1].set_title("f(θ)")
    plt.show()
else:
    print(f"Nenhuma raíz encontrada dentro de {n}  iterações")