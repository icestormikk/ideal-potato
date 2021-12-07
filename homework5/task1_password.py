min_pass_length = 6

def checkPassword(password):
    """Проверка строки-пароля на соответствие условиям,
    установленным в задании 1 (занятие 5).
    
    Аргументы:
    password - строка-пароль для проверки
    
    Исключения:
    ValueError, если пароль не соответветствует хотя бы одному условию.
    Ошибка содержит информацию о нарушенном условии.
    """
    
    if (len(password) < min_pass_length):
        raise ValueError("Слишком короткий пароль.");
    elif ({x for x in password}.intersection({str(i) for i in range(10)}).__len__() == 0):
        #если множество из символов принятой строки не пересекается с множеством из цифр, то возвращаем False (или бросаем исключение)
        raise ValueError("Требуется как минимум одна цифра.");
    elif (str(password).isnumeric()):
        raise ValueError("Пароль не может состоять только из цифр.");
    elif (str(password).lower().__contains__("password")):
        raise ValueError("Пароль не может содержать слово \"password\".");
    else:
        return True;

def isPassword(password):
    """Проверка строки-пароля на соответствие условиям,
    установленным в задании 1 (занятие 5).
    
    Аргументы:
    password - строка-пароль для проверки.
    
    Возвращает True, если пароль соответствует треблованиям, иначе False.
    """
    if (len(password) < min_pass_length):
        return False;
    elif ({x for x in password}.intersection({str(i) for i in range(10)}).__len__() == 0):
        return False;
    elif (str(password).isnumeric()):
        return False;
    elif (str(password).lower().__contains__("password")):
        return False;
    else:
        return True;

#вариант с true|false
if (isPassword(input('Введите строку-пароль (true/false version): '))):
    print("Данная строка может быть паролем");
else:
    print("[!] Строка не может использоваться в качестве пароля")

#вариант с исключениями
try:
    checkPassword(input('\nВведите строку-пароль (exceptions version): '))
    print("Данная строка может быть паролем");
except ValueError as ve:
    print("[!] Строка не может использоваться в качестве пароля\nПричина:", ve.args[0])
