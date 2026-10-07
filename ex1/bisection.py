from math import sin, pi
from matplotlib import pyplot as plt
def f(x):
    return 100**2/9.8*(sin(x) + 0.5*sin(2*x)) - 1000
array = []

def bisection(a, b, e, n):
    k = 0

    array = []
    fa = f(a)
    while k < n:
        k += 1
        x = (a + b)/2
        fx = f(x)
        array.append((x, fx))
        if abs(fx) <= e:
            return array
        if fa * fx < 0:
            b = x
        else:
            fa = fx
            a = x
    return 

a = 0.5
b = 1.5
e = 10**-5
n = 100

array = bisection(a, b, e, n)
if array:
    print(f"O intervalo inicial {(a, b)} convergiu em {len(array)} iterações para {array[-1][0]}")

    fig, ax = plt.subplots(2, 1)

    ax[0].plot([i+1 for i in range(len(array))], [t[0] for t in array], marker = 'o')
    ax[0].set_title("θ")

    ax[1].plot([i+1 for i in range(len(array))], [t[1] for t in array], marker = 'o')
    ax[1].set_title("f(θ)")
    plt.show()
else:
    print(f"Nenhuma raíz encontrada dentro de {n}  iterações")