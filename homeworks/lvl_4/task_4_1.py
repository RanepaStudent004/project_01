# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:



# Cоздание таблицы School
# import sqlite3
# connection = sqlite3.connect('teachers.db')

# cursor = connection.cursor()

# sqlquery = """CREATE TABLE School (
# School_Id INTEGER NOT NULL PRIMARY KEY,
# School_Name TEXT NOT NULL
# );"""

# cursor.execute(sqlquery)

# connection.commit()
# connection.close()

# Вставка значений в таблицу School
# import sqlite3
# connection = sqlite3.connect('teachers.db')
# cursor = connection.cursor()

# sqlquery = """INSERT INTO School (School_Id , School_Name)
# VALUES
# ('1', 'Протон'),
# ('2', 'Преспектива'),
# ('3', 'Спектр'),
# ('4', 'Содружество');"""

# cursor.execute(sqlquery)

# connection.commit()
# connection.close()

# Cоздание таблицы Students
# import sqlite3

# connection = sqlite3.connect('teachers.db')
# cursor = connection.cursor()

# sqlquery = """CREATE TABLE Students (
# Student_Id INTEGER NOT NULL PRIMARY KEY,
# Student_Name TEXT NOT NULL,
# School_Id INTEGER NOT NULL
# );
# """

# cursor.execute(sqlquery)

# connection.commit()
# connection.close()

# Вставка значений в таблицу Students
# import sqlite3
# connection = sqlite3.connect('teachers.db')
# cursor = connection.cursor()
# sqlquery = """INSERT INTO Students (Student_Id, Student_Name, School_Id)
# VALUES
# ('201', 'Иван', '1'),
# ('202', 'Петр', '2'),
# ('203', 'Анастасия', '3'),
# ('204', 'Игорь', '4');"""
# cursor.execute(sqlquery)
# connection.commit()
# connection.close()

import sqlite3

def get_connection():
  connection = sqlite3.connect('teachers.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def get_student_info(S_Id):
  try:
    connection = get_connection()
    cursor = connection.cursor()
    select_query = "SELECT Students.Student_Id, Students.Student_Name, Students.School_Id, School.School_Name FROM Students JOIN School ON School.School_Id = Students.School_Id AND Students.Student_Id="
    select_query +=str(S_Id)
    select_query +=";"
    cursor.execute(select_query)
    records = cursor.fetchall()
    close_connection(connection)
    for row in records:
      print ("ID Студента:", row[0])
      print ("Имя студента:", row[1])
      print ("ID школы:", row[2])
      print ("Название школы", row[3] , "\n")
      
  except (Exception, sqlite3.Error) as error:
    print ("Ошибка в получении данных: ", error)

x = int(input("Введите ID студента:"))

get_student_info(x)