import random

list1, list2 = set(random.randint(1,50) for x in range(random.randint(5,20))), set(random.randint(1,50) for x in range(random.randint(5,20)))
print(f'Первое множество: {list1}\nВторое множество: {list2}\n')

print(f'Элементы, содержащиеся в обоих множествах одновременно: {list1 & list2}')
print(f'Элементы, входящие в первое множество, но отсутствующие во втором: {list1 - list2}')
print(f'Элементы, входящие во второе множество, но отсутствующие в первом: {list2 - list1}')

list1.symmetric_difference_update(list2)
print(f'Элементы, входящие во первое или второе множество, но не в оба одновременно: {list1}')