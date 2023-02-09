def get_name():
    #  Запрос пользователя на ввод имени
    name = input('Write yo name: ')
    return name

def geert (name): 
    #  Приветствие с пользователем
    print (f'Hello {name}')
 
def main ():
    #  главная функция
    name = get_name()
    geert (name)
   

if __name__ == '__main__':
    print(f'__name__ == {__name__}')
    main()    
    
