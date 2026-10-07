from math import sin, pi
from matplotlib import pyplot as plt
def f(x):
    return 100**2/9.8*(sin(x) + 0.5*sin(2*x)) - 1000

def secant(x1, x2, e, n):
    array = []
    k = 0
    fx1 = f(x1)
    fx2 = f(x2)
    while True:
        k += 1

        if k > n:
            print(f"Não foi possível encontrar raíz dentro de {k}  iterações")
            return

        x1, x2 = x2, (x2 - (x2 - x1)*fx2/(fx2 - fx1))
        fx1, fx2 = fx2, f(x2)
        array.append((x2, fx2))
        if abs(fx2) <= e:
                return array

x1 = 0.7
x2 = 0.8
e = 10**-5
n = 100

array = secant(x1, x2, e, n)

print(f"O chute inicial {(x1, x2)} convergiu em {len(array)} iterações para o valor {array[-1][0]}")

fig, ax = plt.subplots(2, 1)

ax[0].plot([i+1 for i in range(len(array))], [tupla[0] for tupla in array], marker = 'o') # 0 para x e 1 para fx
ax[0].set_title("θ")

ax[1].plot([i+1 for i in range(len(array))], [tupla[1] for tupla in array], marker = 'o') # 0 para x e 1 para fx
ax[1].set_title("f(θ)")
plt.show()
