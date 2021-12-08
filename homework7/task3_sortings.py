import random

def bubble_sort(mass):
    """Сортировка методом пузырька.

    Аргументы:
    mass - массив, который необходимо отсортировать.
    """
    
    for i in range(len(mass) - 1):
        for j in range(len(mass) - i - 1):
            if (mass[j] > mass[j + 1]):
                mass[j + 1], mass[j] = mass[j], mass[j + 1]

def insertion_sort(mass):
    """Сортировка вставками.

    Аргументы:
    mass - массив, который необходимо отсортировать.
    """
    
    for i in range(1, len(mass)):
        to_insert_item = mass[i]
        j = i - 1
        while (j >= 0 and mass[j] > to_insert_item):
            mass[j + 1] = mass[j]
            j -= 1
        mass[j + 1] = to_insert_item

def quick_sort(mass, first_index, last_index):
    """Быстрая сортировка.

    Аргументы:
    mass - массив, который необходимо отсортировать.
    """
    
    if (first_index >= last_index):
        return

    i, j = first_index, last_index
    pivot = mass[random.randint(first_index, last_index)]

    while (i <= j):
        while (mass[i] < pivot):
            i += 1
        while (mass[j] > pivot):
            j -= 1
        if (i <= j):
            mass[i], mass[j] = mass[j], mass[i]
            i, j = i + 1, j - 1
    quick_sort(mass, first_index, j)
    quick_sort(mass, i, last_index)

def nullify(mass):
    """Обнуление значений принимаемого массива
    
    Аргументы:
    mass - массив, который необходимо отсортировать.
    """
    
    for i in range(len(mass)):
        mass[i] = 0;