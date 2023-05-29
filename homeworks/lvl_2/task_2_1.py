# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции sorted, max и min использовать нельзя!


from random import randint

def minimum(arr):
    
    i = 0
    while i < n - 1:
        m = i
        j = i + 1
        while j < n:
            if arr[j] < arr[m]:
                m = j
            j += 1
        arr[i],arr[m] = arr[m],arr[i]
        i += 1
    print("min =",arr[0])
    #print (arr)

def maximum(arr):
    
    i = 0
    while i < n - 1:
        m = i
        j = i + 1
        while j < n:
            if arr[j] > arr[m]:
                m = j
            j += 1
        arr[i],arr[m] = arr[m],arr[i]
        i += 1
    print("max =",arr[0])
   # print (arr)

n = 8
arr = []

for i in range(n):
   arr.append(randint(-100,100))
print (arr)

minimum(arr)

maximum(arr)