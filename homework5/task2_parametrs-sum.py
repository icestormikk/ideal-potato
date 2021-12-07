from math import sqrt

def summation(*args):
    """Сложение всех переданных аргументов.
    
    Аргументы:
    данные любого типа, для которого возможна операция сложения.
    
    Исключения:
    TypeError, если переданные аргументы невозможно сложить
    (несоответствие типа).
    """
    if (len(args) > 0):
        result = args[0];
        for i in range(1,len(args)):
            #весь код в этом блоке можно заменить двумя командами: result + args[i]; result += args[i]
            try: 
                result + args[i];
            except TypeError as te:
                raise te
            else:
                result += args[i]
        return result;
    return 0;

print(f'[1] Сумма целых чисел от 1 до 10: {summation(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}')
print(f'\n[2] Получение предложения путём соединения n-ого кол-ва слов: {summation("Sun", " is", " shining", " and", " so", " are", " you")}')
print(f'\n[3] Сложение кортежей: {summation((1, 2, 3), (4, 5, 6), (7, 8, 9))}');

print(f'\n[4] Попытка сложить множество и список:');
try:
    print(summation([x for x in range(10)], {x for x in "Hello World"}))
except TypeError as te:
    print("\t[!] Переданные данные невозможно сложить\n\t[INFO]", te.args[0]);

print(f'\n[5] Сложение списка и строки:');
try:
    print(summation([sqrt(x) for x in range(100)], ""), "Just three words")
except TypeError as te:
    print("\t[!] Переданные данные невозможно сложить\n\t[INFO]", te.args[0]);

print(f'\n[6] Сложение кортежа и списка: ')
try:
    print(summation((0, 1, 2, 3, 4, 5), ['a', 'b', 'c', 'd']))
except TypeError as te:
    print("\t[!] Переданные данные невозможно сложить\n\t[INFO]", te.args[0]);
