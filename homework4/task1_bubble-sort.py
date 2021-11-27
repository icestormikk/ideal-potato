import random;

def bubble_sort(mass):
    for i in range(len(mass) - 1):
        for j in range(len(mass) - i - 1):
            if (mass[j] > mass[j+1]):
                mass[j+1], mass[j] = mass[j], mass[j+1];

list = [(random.random() * 100) for x in range(random.randint(5,20))]
print(f'Исходный массив: {list}')
bubble_sort(list)
print(f'\nОтсортированный массив: {list}')
