# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

print('your current directory is {}'.format(os.getcwd()))
def makedir(i):
    os.mkdir('{}'.format(i))
def removedir(i):
    os.rmdir('{}'.format(i))
def chdir(i):
    os.chdir(i)
for j in range(9):
    makedir('dir_{}'.format(j + 1))
#print(os.listdir())

for j in range (9):
    removedir('dir_{}'.format(j + 1))




# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


def list_directory():
    print('the current directory has {}'.format(os.listdir()))


#print(current_directory)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


def createfile_indirectory():
    os.popen('cp python5easy.py python5easy01.py') 
    #cp вместо copy так как я сижу на мак буке ) 


