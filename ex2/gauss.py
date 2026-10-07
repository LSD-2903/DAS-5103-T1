def gauss(A, b):
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

eq1 = [-1, 0, 0, 0, 0, 0, 2]
eq2 = [1, -1, 0, 0, 0, 0, 0]
eq3 = [0, 1, -1, 0, 0, 0, 0]
eq4 = [0, 0, 1, -1, 0, 0, 0]
eq5 = [0, 0, 0, 1, -1, 0, 0]
eq6 = [0, 0, 0, 0, 0, 1, 0]
eq7 = [0, 0, 0, 0, 1, 1, -1]
b = [0, -130, 102, 22, -1, 29, 38]
A = [eq1, eq2, eq3, eq4, eq5, eq6, eq7]

print(gauss(A, b))
