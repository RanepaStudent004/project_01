import random


my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

R = random.sample(my_favorite_songs, 3, counts=None)   # выбираем 3 случайные песни
print(R)

Time3songs = 0

for i in R:          # складываем
    Time3songs += i[1]

print(f'Три песни звучат {round(Time3songs,2)} минут')


my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}


l=len(my_favorite_songs_dict) # количество элементов словаря 
print("Всего песен = ",l)
U = 0   # переменная для суммирования времени песен
for g in range(0,3):  # выбираем 3 песни
 i = random.randrange(l) # случайное число от 0 до 9(не включительно) выбирается 3 раза 
 #print(i)
 # используем случайное число для доступа к элементу словря
 U = U+my_favorite_songs_dict[list(my_favorite_songs_dict.keys())[i]]
 print(my_favorite_songs_dict[list(my_favorite_songs_dict.keys())[i]]) 
print(f'Три песни звучат {round(U,2)} минут')



