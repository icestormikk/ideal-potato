import os
import re

#Формат ввода: X = Y (X - символ химического элемента, Y - кол-во атомов элемента X)
#Разделитель: запятая
#Пример: C = 2, H = 6, O = 1
elements = []
elements_coeffs = dict()

try:
    with open("input.txt", "rt") as f:
        elements = re.split(",\W*", f.read())
except FileNotFoundError:
    print("[!] Не найден файл с именем input.txt")
    exit()

if (len(elements) == 3):
    for i in elements:
        if (re.fullmatch("[C,H,O]\s*=\s*[0-9]+", i)):
            elements_coeffs[i.replace(" ","").split("=")[0]] = int(i.replace(" ","").split("=")[1])
        else:
            print("[!] Нарушен формат ввода.)")
            print("Возможные ошибки:\n    (1) Введён иной химический элемент (не С, H или O)")
            print("    (2) Неправильный ввод кол-ва атомов элемента")
            print("    (3) Введён лишний разделитель")
            exit()
    if (len(elements_coeffs) != len(elements)):
        print("[!] Нарушен формат ввода.\n    Возможные ошибки:\n")
        print("    (1) Переопределено кол-во некоторого элемента")
        exit()
else:
    print("[!] Ошибка ввода: ", end='')
    if (len(elements) < 3):
        print("введено недостаточное кол-во элементов")
    else:
        print("введено излишнее кол-во элементов")
    exit()

file_name = "output.txt"
with open(file_name,"w") as file:
    file.write(str(int(min([elements_coeffs.get("C") / 2, elements_coeffs.get("H") / 6, elements_coeffs.get("O")]))))
    # одна молекула этилового спирта содержит 2 атома углерода, 6 атомов водорода и 1 атом кислорода
    # кол-во возможных молекул найдём по следующей формуле: 
    # min(n(C)(общ.) / n(C)(в одной мол.), n(H)(общ.) / n(H)(в одной мол.), n(O)(общ.) / n(O)(в одной мол.)),
    #    где n(X) - кол-во атомов элемента X 
    # поскольку кол-во молекул может быть только целым числом, возьмём лишь целую часть от получившегося числа
    print("Результат сохранён в файл", os.path.realpath(file_name))
