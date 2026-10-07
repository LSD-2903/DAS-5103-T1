from math import sin, pi
from matplotlib import pyplot as plt
def f(x):
    return 100**2/9.8*(sin(x) + 0.5*sin(2*x)) - 1000
array = []

def bissecção(a, b, e, n):
    k = 0
    array = []
    fa = f(a)
    while True:
        k += 1
        if k > n:
            print(f"Não foi possível encontrar raíz dentro de {k}  iterações")
            return 
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

a = 0.5
b = 1.5
e = 10**-5
n = 100

array = bissecção(a, b, e, n)

print(f"O chute inicial {(a, b)} convergiu em {len(array)} iterações para o valor {array[-1][0]}")

fig, ax = plt.subplots(2, 1)

ax[0].plot([i+1 for i in range(len(array))], [tupla[0] for tupla in array], marker = 'o') # 0 para x e 1 para fx
ax[0].set_title("θ")

ax[1].plot([i+1 for i in range(len(array))], [tupla[1] for tupla in array], marker = 'o') # 0 para x e 1 para fx
ax[1].set_title("f(θ)")
plt.grid(True)
plt.show()