import os

print("Имя операционной системы:", end=' ')
try:
    print(os.uname()[0]) # вариант для Unix/Linux
except AttributeError:
    print(os.name) # вариант для Windows

print(f'Имя пользователя, вошедшего в терминал: {os.getlogin()}')

if (input('\nЖелаете указать путь к папке, содержимое которой хотите просмотреть? (y/n) ') == 'y'):
    try:   
        for i in os.listdir(path=input('Введите путь: ')):
            print("\t", i)
        exit()
    except FileNotFoundError:
        print("[!] Не удалось найти папку по данному пути")
    except PermissionError:
        print("[!] Отсутствует доступ к данному каталогу")

print(f'Содержимое текущего каталога ({os.getcwd()}):')
for i in os.listdir(os.getcwd()):
    print("\t", i)
