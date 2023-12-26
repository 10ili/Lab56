from tkinter import*
from PIL import Image,ImageTk
def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1, i,-1):
            if arr[i] < arr[j-1]:
                arr[j],arr[j-1] = arr[j-1],arr[j]
    return arr
def ozidanie(f):
    p = 1/len(f)
    summ = 0
    for i in range(len(f)):
        summ += f[i]
    p *= summ
    return p
sort_1 = []
A = [0.48, 0.51, 0.71, 0.6]
B = [0.95, 1.1, 1.01, 1.25, 0.99]
C = [0.85, 0.93, 0.7, 0.75, 0.8]
sort_1.append(ozidanie(A))
sort_1.append(ozidanie(B))
sort_1.append(ozidanie(C))
sort_1 = bubbleSort(sort_1)
window = Tk()
window.title('Лабораторная работа 5 Маслов Илья')
window.geometry('1000x500')
img = ImageTk.PhotoImage(Image.open('Лаб 5.jpg.png'))
b = Label(image=img)
b.grid(row=5,column=5)
lbl = Label(window, text = 'A = ' + str(A)).grid(row=0,column=1,sticky=W)
lbl = Label(window, text = 'B = ' + str(B)).grid(row=1,column=1,sticky=W)
lbl = Label(window, text = 'C = ' + str(C)).grid(row=2,column=1,sticky=W)
lbl = Label(window, text = 'Математическое ожидание = ' + str(sort_1)).grid(row=3,column=1,sticky=W)

window.mainloop()
print(sort_1)