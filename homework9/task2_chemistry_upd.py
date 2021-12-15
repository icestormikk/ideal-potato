import os
import re

#   Усовершенствованная задача №2 из 6-ой домашней работы
#
#   Сначала на вход подаётся набор атомов (чтение из файла input.txt): запись ведётся в том же формате, 
# что и в прошлой д/з + допускается запись в виде названия соединения (допустимые соединения перечислены в
# словаре compounds (при желании можно расширить)). Набор хранится в виде словаря elements_countainer.
#
#   После успешной обработки происходит запрос формулы у пользователя. Допустимый формат записи: X(Y), где
# X - элемент из списка elements_container, Y - натуральное число. Пример: C(2)H(4)O(2)
#
#   Дальнейшая работы функции совпадает с работой её "простой" версии.

compounds = dict(
    oxytocine = dict(C = 43, H = 66, N = 12, O = 12, S = 2),
    dopamine = dict(C = 8, H = 11, N = 1, O = 2),
    serotonin = dict(C = 10, H = 12, N = 2, O = 1),
    adrenaline = dict(C = 9, H = 13, N = 1, O = 3),
    triiodothyronine = dict(C = 15, H = 12, I = 3, N = 1, O = 4),
    insulin = dict(C = 257, H = 383, N = 65, O = 77, S = 6),
    ethanol = dict(C = 2, H = 6, O = 1)
)
elements = [] # список для выражений, считанных из input.txt
elements_container = dict() # словарь с "набором" атомов
elements_formula = dict() # словарь с набором атомов, из которых состоит введённая молекула

class UnknownElementError(Exception):
    def __init__(self, message):
        super().__init__(message)

class WrongInputError(Exception):
    def __init__(self, message=""):
        super().__init__(message)

def molecula_count(molecula: str):
    try:
        with open("input.txt", "rt") as f:
            elements = re.split(",\W*", f.read())
    except FileNotFoundError:
        print("[!] Не найден файл с именем input.txt")
        exit()

    for i in elements:
        if (len(i) == 0):
            continue
        if (re.fullmatch("[A-Za-z]{1,2}\s*=\s*[0-9]+", i)):
            line = i.replace(" ","").split("=")[0]
            if (elements_container.__contains__(line)):
                elements_container[line] += int(i.replace(" ","").split("=")[1])
            else:
                elements_container[line] = int(i.replace(" ","").split("=")[1])
        elif (re.fullmatch("[A-Za-z]+,*", i)):
            if (compounds.__contains__(i.lower())):
                for compound, elems in compounds.items(): # пробегаем все элементы словаря compounds 
                    if (compound == i): #пока не найдём нужный нам
                        for elem, count in elems.items(): # поэлементно считываем инф-цию об атомах этого соединения
                            if (elements_container.__contains__(elem)):
                                elements_container[elem] += count
                            else:
                                elements_container[elem] = count
                    else:
                        pass
            else:
                if (i == "Olya"):
                    raise UnknownElementError(f'{i} is sweetie_pie, not chemical compound.')
                raise UnknownElementError("Неизвестное соединение")
        else:
            raise WrongInputError("Ошибка ввода элементов набора.")

    for i in re.split("\)+", molecula):
        if (len(i) == 0):
            continue
        if (re.fullmatch("[A-Za-z]{1,2}\([0-9]+", i)):
            elem_name = i.replace(" ","").split("(")[0]
            if (elements_container.__contains__(elem_name)):
                if (int(i.replace(" ","").split("(")[1]) > 0):
                    if (elements_formula.__contains__(elem_name)):
                        elements_formula[elem_name] += \
                            int(i.replace(" ","").split("(")[1])
                    else:
                        elements_formula[elem_name] = \
                            int(i.replace(" ","").split("(")[1])
                else:
                    pass
            else:
                raise UnknownElementError(f'Элемент {i.replace(" ","").split("(")[0]} не содержится в наборе элементов.')
        else:
            raise WrongInputError("Ошибка ввода формулы")

    min = None
    for key, value in elements_formula.items():
        if (min is None):
            min = elements_container.get(key) / elements_formula.get(key)
        else:
            if (elements_container.get(key) / elements_formula.get(key) < min):
                min = elements_container.get(key) / elements_formula.get(key)

    file_name = "output.txt"
    with open(file_name,"w") as file:
        file.write(str(int(min)))
        print("Результат сохранён в файл", os.path.realpath(file_name))
