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