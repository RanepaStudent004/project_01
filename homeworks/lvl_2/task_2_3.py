# Задача 2.3.

# Напишите функцию, которая принимает цифры от 0 до 9 и возвращает значение прописью.
# Например,
# switch_it_up(1) -> 'One'
# switch_it_up(3) -> 'Three'
# switch_it_up(10000) -> None
# Использовать условный оператор if-elif-else нельзя!


def switch_it_up(number):
   N = ["zero","one","two","three","four","five","six","seven","eight","nine"] 
   result=N[number]
   return result


try:
    m = int(input("Введите цифру:  "))
    if -1<m<10:
        print(switch_it_up(m))
    else:
            print("None")
except:
    print("None")