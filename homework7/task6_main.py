import random
import time

import task3_sortings as srts

size = random.randint(1,20)
for i in range(3):
    mass = [random.randint(1,100) for x in range(size)]

    start_time = time.perf_counter()
    print("\nНачальный массив:", mass, "\nОстортированный массив ", end='')
    match i:
        case 0:
            print("(сортировка пузырьком)", end='')
            srts.bubble_sort(mass)
        case 1:
            print("(сортировка вставками)", end='')
            srts.insertion_sort(mass)
        case 2:
            print("(быстрая сортировка)", end='')
            srts.quick_sort(mass, 0, len(mass) - 1)
    print(":", mass, "\nВремя выполнения:", time.perf_counter() - start_time)
print("Обнуление массива:", mass, "-> ", end='')
srts.nullify(mass)
print(mass)
