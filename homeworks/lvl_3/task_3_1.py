from pickle import LIST

class MyMatrixRow(list):   # MMR = объект этого класса 
    def add_var(self, v):
        self.append(v)
    def rows(self, x):       
        result = self[x]
        return result

class MyMaster(list):     # Master = объект этого класса 
     def add_row(self, vMMR): # добавляем объект  в конец списка
          self.append(vMMR)
     def rows(self, y, x):
         result = self[y][x]
         return result
     def value(self, y, x, v):
         self[y][x] = v


# основной код
Master = MyMaster()   # создать объект Master
print("заполняем матрицу 0")
for y in range(0, 5):
    MMR = MyMatrixRow()  # создать объект MMR       
    for x in range(0, 5):   
        MMR.add_var("0")     

    Master.add_row(MMR)

for y in range(0, 5): # выводим значения в матрице
    s = ""
    for x in range(0, 5):
        s += Master.rows(y, x)
        s +=", "
    print(s)

print("Количество строк: ", len(Master))
print("Количество колоник: ", len(MMR))
print("заменяем существующие значения")
for y in range(0, 5):           
     for x in range(0, 5):             
         Master.value(y, x, str(x+y*10))

for y in range(0, 5): # выводим новые значения в матрице
    s = ""
    for x in range(0, 5):
        s += Master.rows(y, x)
        s +=", "
    print(s)