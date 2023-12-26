import math
from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.title('Лабораторная работа 6 Маслов Илья вар 15')
window.geometry('1100x600')


def matrix(d, n):
    A = [[(0) for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if i > j + 2:
                A[i][j] = float('{:.3f}'.format((d ** 2) * (i + 1) + (0.938 * (j + 1)) ** 2))
            else:
                A[i][j] = float('{:.3f}'.format(math.atan((i * math.pi / (j + 1) + 0.387))))
    return A


A = matrix(5, 9)
with open("Лабораторная работа 6.txt", "w") as file:
    file.write('Ishodnay matriza' + '\n')
    file.write('\n'.join('\t'.join(map(str, row)) for row in A))
lbl = Label(window, text='Исходаня матрица').grid(row=0, column=1, sticky=NW)
lbl = Label(window, text=str('\n'.join('\t'.join(map(str, row)) for row in A))).grid(row=1, column=1, sticky=W)


def obrabotka(n):
    A = matrix(5, 9)
    C = A[5]
    F = A[6]
    A[6] = C
    A[5] = F
    return A


B = obrabotka(9)
with open("Лабораторная работа 6.txt", "a+") as file:
    file.write('\n' + 'Obrabotannay matriza' + '\n')
    file.write('\n'.join('\t'.join(map(str, row)) for row in B))
lbl = Label(window, text='Обработанная матрица').grid(row=11, column=1, sticky=NW)
lbl = Label(window, text=str('\n'.join('\t'.join(map(str, row)) for row in B))).grid(row=12, column=1, sticky=W)
lbl = Label(window, text=('Минимальный элемент - ')).grid(row=13, column=1, sticky=W)


def minimal(n):
    A = matrix(5, 9)
    minn = min(A)
    return minn


p = minimal(9)
with open("Лабораторная работа 6.txt", "a+") as file:
    file.write('\n' + 'Minimalniy element = ' + str(p[0]))
lbl = Label(window, text=('Минимальный элемент - ' + str(p[0]))).grid(row=13, column=1, sticky=W)


def vector(n):
    X = []
    A = matrix(5, 9)
    for i in range(n):
        for j in range(n):
            if j == 2:
                X.append(A[i][j])
    for i in range(len(X)):
        for j in range(len(X) - 1):
            if X[j] > X[j + 1]:
                X[j], X[j + 1] = X[j + 1], X[j]
    return X


o = vector(9)
with open("Лабораторная работа 6.txt", "a+") as file:
    file.write('\n' + 'Vector X = ' + str(o))
lbl = Label(window, text=('Вектор X = ' + str(o))).grid(row=14, column=1, sticky=W)
img = ImageTk.PhotoImage(
    Image.open("Лаб 6.png"))
b = Label(image=img)
b.grid(row=20, column=1, sticky=W)

window.mainloop()
