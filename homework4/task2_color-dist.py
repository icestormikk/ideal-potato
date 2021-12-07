from random import randint

colorDict = {"red":tuple([255, 0, 0]),"green":tuple([0, 255, 0]), "blue":tuple([0, 0, 255])}

def duplicateColor(colorName):
    """Проверка на содержание цвета с именем colorName
    в словаре цветов colorDict.
    
    Аргументы:
    colorName - название нового цвета
    """
    
    return not colorDict.keys().isdisjoint([colorName])

while True:
    user_in = input('\nВведите действие (addColor/showAll/removeColor/clear/exit): ');
    if (user_in == "addColor"):
        new_color = input('\tВведите название цвета: ')
        if (duplicateColor(new_color)):
            print("\t[!] Цвет с таким именем уже есть в словаре")
        else:
            try:
                rgb_values = [int(x) for x in input('\tВведите код цвета в RGB (через пробел): ').split(" ")]
                colorDict[new_color] = tuple(rgb_values)
                for i in colorDict[new_color]:
                    if (i > 255 or i < 0):
                        raise ValueError(f'[INFO] Введённое значение не входит в диапазон [0, 255]: {i} <-')
            except ValueError as wrong_value:
                print("\t[!] Ошибка при вводе значений цвета в системе RGB\n\t", wrong_value.args[0])
                if (colorDict.__contains__(new_color)):
                     colorDict.__delitem__(new_color)
                continue
            print("\t[DONE] Новый цвет успешно добавлен к словарь.");
    elif (user_in == "showAll"):
        if (len(colorDict) > 0):
            print("%-15s%-10s" % ("Color Name", "RGD-Code"))
            for key,value in colorDict.items():
                print("%-15s%-10s" % (key,value))
        else:
            print("[!] Список цветов пуст.")
    elif (user_in == "removeColor"):
        try:
            colorDict.__delitem__(input('\tВведите название удаляемого цвета: '))
        except KeyError:
            print("\t[!] Цвет с таким названием отсутствует в словаре")
    elif (user_in == "clear"):
        colorDict.clear();
    elif (user_in == "exit"):
        break;
    else: 
        print("[!] Не удалось распознать команду. Повторите ввод.")
