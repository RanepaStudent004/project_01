# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"


print("Пункт А:")

def remove_exclamation_marks(f):
    result = f.replace('!', '') 
    return result
    

foo1 = "Hi! Hello!"
foo2 = ""
foo3 = "Oh, no!!!"

print(remove_exclamation_marks(foo1))
print(remove_exclamation_marks(foo2))
print(remove_exclamation_marks(foo3))


print("Пункт B:")
# Удалите восклицательный знак из конца строки. 

def remove_last_em(s):
     
   v=-1 # начальное условие, если нет ! в строке
   r = list(s)
   i = len(s)-1  # указываем последний символ в строке
   if s[i]=="!":
        v=i
        
  
   if v>-1:
        r.pop(v) # удаляем элемент с индексом v
   result = ''.join(r) # переводим список в строку
   return result


remove1 = "Hi!"
remove2 = "Hi!!!"
remove3 = "!Hi"

print(remove_last_em(remove1))
print(remove_last_em(remove2))
print(remove_last_em(remove3))

