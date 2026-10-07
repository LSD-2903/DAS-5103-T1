def gauss(A, b):
    n  = len(A)
    for i in range(n):
        pivot = i
        for j in range(i + 1, n):
            if abs(A[j][i]) > abs(A[pivot][i]):
                pivot = j

        if pivot != i:
            A[i], A[pivot] = A[pivot], A[i]
            b[i], b[pivot] = b[pivot], b[i]

        if A[i][i] == 0:
            print("A matriz é singular")
            return
        
        for j in range(i + 1, n):
            multiplier = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] = A[j][k] - multiplier * A[i][k]
            b[j] = b[j] - multiplier * b[i]

    x = [0] * n

    for i in range(n - 1, -1, -1):
        sum = 0

        for j in range(i + 1, n):
            sum += A[i][j] * x[j]
        x[i] = (b[i] - sum) / A[i][i]
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
