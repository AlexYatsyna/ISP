import math
c = [[0.01, 0, -0.02, 0, 0], [0.01, 0.01, -0.02, 0, 0], [0, 0.01, 0.01, 0, -0.02], [0, 0, 0.01, 0.01, 0], [0, 0, 0, 0.01, 0.01]]
d = [[1.33, 0.21, 0.17, 0.12, -0.13], [-0.13, -1.33, 0.11, 0.17, 0.12], [0.12, -0.13, -1.33, 0.11, 0.17], [0.17, 0.12, -0.13, -1.33, 0.11], [0.11, 0.67, 0.12, -0.13, -1.33]]
b = [1.2, 2.2, 4.0, 0.0, -1.2]
n = 5
k = 0
a = [[0] * n for i in range(n)]
isAnswer = False
x = [0] * n
temp = [0] * n
approximations = [0] * n
sufficientCondition = True
maxValue = 0
maxIndex = 0
for i in range(n):
    for j in range(n):
        a[i][j] = round(c[i][j] * k + d[i][j], 4)
print("A:")
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end='\t')
    print('\n')
for i in range(len(a)):
    if a[i][i] == 0:
        sufficientCondition = False
if sufficientCondition:
    for i in range(n):
        maxValue = math.fabs(a[i][i])
        for j in range(i + 1, n):
            if math.fabs(a[j][i]) > maxValue:
                maxIndex = j
                maxValue = math.fabs(a[j][i])
        if maxValue != math.fabs(a[i][i]):
            for j in range(n):
                temp[j] = a[maxIndex][j]
            tempB = b[maxIndex]
            for j in range(n):
                a[maxIndex][j] = a[i][j]
            b[maxIndex] = b[i]
            for j in range(n):
                a[i][j] = temp[j]
            b[i] = tempB
    for i in range(n ** 5):
            if i != 0:
                for j in range(n):
                    if math.fabs(math.fabs(x[j]) - math.fabs(approximations[j])) <= 0.00001:
                        isAnswer = True
                    else:
                        isAnswer = False
            if not isAnswer:
                for j in range(n):
                    approximations[j] = x[j]
                for j in range(n):
                    x[j] = b[j] / a[j][j]
                    for k in range(n):
                        if j != k:
                            x[j] -= a[j][k] * x[k] / a[j][j]
            else:
                break
print('x:')
for i in range(n):
    print(round(x[i], 3))
while True:
    pass
