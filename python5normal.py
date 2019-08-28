# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
import python5easy as python
import sys
import os


print('1.Go to directory \n2.Check whats inside a directory\n3.Remove directory\n4.Make a directory')
user_input = int(input('Enter your choice'))
if user_input == 1:
    move_path = input('Enter a path: (WINDOWS start with disc, LINUX/UNIX start with /')
    try:
        os.chdir(move_path)
        print('You have moved to a directory')
    except NotADirectoryError:
        print('This directory doesnt exist!')
    
elif user_input == 2:
    python.list_directory()
    print('directories listed')

elif user_input == 3:
    i = input('Enter a directory to be deleted')
    try:
        python.removedir(i)
        print('current directory deleted successfully')
    except NotADirectoryError:
        print('failed to delete directory')
        
elif user_input == 4:
        i = input('Enter directory name')
        try:
            python.makedir(i)
        except FileExistsError:
            print('this directory already exists')







    










