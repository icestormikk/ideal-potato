def xor_encode(string, key):
    res = bytearray()
    for i in range(len(string)):
        res.append(string[i] ^ key[i % len(key)])
    return res

def xor_decode(byteline, key):
    res = bytearray()
    for i in range(len(byteline)):
        res.append(byteline[i] ^ key[i % (len(key))])
    return res

encoding_text = ""
try:
    with open(input('Введите имя файла с текстом для шифрования: '), "rb") as f:
        encoding_text = f.read()
except FileNotFoundError:
    print("[!] Не удалось найти файл по заданному пути")
    exit()

if (len(encoding_text) > 0):
    print("XOR-шифрование")
    xorE = xor_encode(encoding_text, bytes(input('  Введите ключ-слово: '), encoding='utf-8'))
    print("  Результат шифрования:", xorE.decode('utf-8', errors='ignore'))

    print("\nXOR-дешифрование")
    print("  Результат дешифровки:", xor_decode(xorE, bytearray(input('  Введите ключ-слово: '), encoding='utf-8')).decode('utf-8', errors='ignore'))
else:
    print("[!] Файл пуст, нечего шифровать")
