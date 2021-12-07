def encodeStrings(lines):
    """Перевод списка строк в список байт-кодов.
   
    Аргументы:
    lines - список строк.
    """
    result = []
    for i in lines:
        if (len(i) != 0):
            result.append(i.encode('utf-8'))
    return result

def decodeStrings(lines):
    """Перевод списка байт-кодов в список из строк.
   
    Аргументы:
    lines - список байт-кодов.
    """
    result = []
    for i in lines:
        if (len(i) != 0):
            result.append(i.decode('utf-8'))
    return result

encodedStrings = []
try:
    with open(input("Введите путь к файлу со строками: "), "r", encoding='utf-8') as f:
        encodedStrings = encodeStrings(f.read().split("\n"))
    print("Результат перевода:", encodedStrings)
except FileNotFoundError:
    print("[!] Не удалось найти файл по введённому пути.\n")

with open("bytes.bin", "wb") as f:
    for i in encodedStrings:
        f.write(i)

if (len(encodedStrings) != 0):
    if (input("\nЖелаете декодировать строки с предыдущего шага? (y/n) ") == 'y'):
        print("Результат обратного перевода", decodeStrings(encodedStrings)); exit()

try:
    with open(input("Введите путь к файлу со строками из байт-кодов: "), "rb") as f:
        print("Результат обратного перевода:", decodeStrings(f.readlines()))
except FileNotFoundError:
    print("[!] Не удалось найти файл по введённому пути.")
