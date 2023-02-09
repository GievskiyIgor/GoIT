#  Аргументы командной строки
#  комманда ls - показывает, что есть в папке
#  as - псевдоним
import sys
# вызываем главные функции из файла welcome and goodbye
from welcome import main as greeting
from goodbye import main as exiting

def main():
    
    if sys.argv[1] == 'greet':
        greeting()
    elif sys.argv[1] == 'goodbye':
        exiting ()        
    
    #  print (sys.argv)
    #  argv - аргумент функции sys, выводит названеи файла и где он находится


if __name__ == '__main__':
    print(f'__name__ == {__name__}')
    main()
