from math import exp
from matplotlib import pyplot as plt
from ex2.gauss import gauss
l = 32000
d = 0.6
As = 60319
ad = 0.2827
m = 44
tsource = 10
tamb = 4
rho = 950
v = 0.1638
cp = 2100
u = 0.510
nbomba = 0.75
celet = 0.17
ccalor = 0.05

def f(x):
    dp = x[0]
    tin = x[1]
    tout = x[2]
    mi = x[3]
    return [dp*10**6 - 32*mi*l*v/d**2,
        m*cp*(tin - tout) - u*As*((tin - tamb) + (tout - tamb))/2,
        6100 - dp*10**6*m*celet*24/(1000*nbomba*rho) - m*cp*(tin -tsource)*ccalor*24/1000,
        mi - 1100*exp(-0.1*(tin+tout)/2)]

def jf(x):
    dp = x[0]
    tin = x[1]
    tout = x[2]
    mi = x[3]
    return [[10**6, 0, 0, -32*l*v/d**2],
    [0, m*cp-u*As/2, m*cp*-1-u*As/2, 0],
    [-10**6*m/(1000*nbomba*rho)*celet*24, -m*cp/1000*ccalor*24, m*cp/1000*ccalor*24, 0],
    [0, -1100*-0.1/2*exp(-0.1*(tin+tout)/2), -1100*-0.1/2*exp(-0.1*(tin+tout)/2), 1]
]

    n  = len(A)
    for i in range(n):
        pivo = i
        for j in range(i + 1, n):
            if abs(A[j][i]) > abs(A[pivo][i]):
                pivo = j

        if pivo != i:
            A[i], A[pivo] = A[pivo], A[i]
            b[i], b[pivo] = b[pivo], b[i]

        if A[i][i] == 0:
            print("Matriz sem solução única")
            return
        
        for j in range(i + 1, n):
            fator = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] = A[j][k] - fator * A[i][k]
            b[j] = b[j] - fator * b[i]

    x = [0] * n

    for i in range(n - 1, -1, -1):
        soma = 0

        for j in range(i + 1, n):
            soma += A[i][j] * x[j]
        x[i] = (b[i] - soma) / A[i][i]
    return x

def newtonRaphson(x, e, n):
    k = 0
    m = len(x)
    array = []
    while k < n:
        A = gauss(jf(x), f(x))
        x1 = [x[i] - A[i] for i in range(m)]
        array.append((x1, f(x1)))
        if max(abs(x1[i]-x[i]) for i in range(m)) < e:
            return array
        x = x1
        k+= 1

x1 = [1, 12, 10, 0.05]
x2 = [15, 25, 10, 1]
e = 10**-5
n = 100

array1 = newtonRaphson(x1, e, n)
print(f"O chute inicial {x1} convergiu em {len(array1)} iterações para os valores {array1[-1][0]}")
array2 = newtonRaphson(x2, e, n)
print(f"O chute inicial {x2} convergiu em {len(array2)} iterações para os valores {array2[-1][0]}")

deltap1 = [item[0][0] for item in array1]
t_in1   = [item[0][1] for item in array1]
t_out1  = [item[0][2] for item in array1]
mi_med1 = [item[0][3] for item in array1]

iteracoes1 = range(len(array1))


deltap2 = [item[0][0] for item in array2]
t_in2   = [item[0][1] for item in array2]
t_out2  = [item[0][2] for item in array2]
mi_med2 = [item[0][3] for item in array2]

iteracoes2 = range(len(array2))

fig, ax = plt.subplots(2, 2, figsize=(12, 8))

ax[0, 0].plot(iteracoes1, deltap1, label=r'$\Delta p$')
ax[0, 0].plot(iteracoes1, mi_med1, label=r'$\mu_{med}$')

ax[0, 0].set_title('Exemplo 1')
ax[0, 0].set_xlabel('Iteração')
ax[0, 0].set_ylabel('Valor')
ax[0, 0].legend()
ax[0, 0].grid()

ax[0, 1].plot(iteracoes2, deltap2, label=r'$\Delta p$')
ax[0, 1].plot(iteracoes2, mi_med2, label=r'$\mu_{med}$')

ax[0, 1].set_title('Exemplo 2')
ax[0, 1].set_xlabel('Iteração')
ax[0, 1].set_ylabel('Valor')
ax[0, 1].legend()
ax[0, 1].grid()

ax[1, 0].plot(iteracoes1, t_in1, label=r'$t_{in}$')
ax[1, 0].plot(iteracoes1, t_out1, label=r'$t_{out}$')

ax[1, 0].set_title('Exemplo 1')
ax[1, 0].set_xlabel('Iteração')
ax[1, 0].set_ylabel('Temperatura')
ax[1, 0].legend()
ax[1, 0].grid()

ax[1, 1].plot(iteracoes2, t_in2, label=r'$t_{in}$')
ax[1, 1].plot(iteracoes2, t_out2, label=r'$t_{out}$')

ax[1, 1].set_title('Exemplo 2')
ax[1, 1].set_xlabel('Iteração')
ax[1, 1].set_ylabel('Temperatura')
ax[1, 1].legend()
ax[1, 1].grid()

plt.tight_layout()
plt.show()
