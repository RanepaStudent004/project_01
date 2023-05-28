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