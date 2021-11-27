maxWeight = 90
inventory = [["Witcher's steel sword", 1, 1.74], ["Wolf School Medallion", 1, 0.5], ["Swallow", 10, 0.1], ["A letter (with the scent of lilac and gooseberries)", 1, 0.0],
["Hunting gauntlets", 1, 0.67], ["Kaer Morhen armor", 1, 1.57], ["Hunting trousers", 1, 1.06], ["Hunting boots", 1, 0.71]]

def duplicateItem(name, weigth = None):
    for i in inventory:
        if (i[0] == name):
            if (weigth != None): #если передан вес предмета
                if (i[2] == weight): #и он равен искомому
                    return i;
                else: 
                    return False
            else: #вес не был передан, проверка по имени прошла успешно
                return i
        #объект не прошёл проверку ни по имени, ни по весу
    return False

def totalInventoryWeight():
    result = 0
    for i in inventory:
        result += i[1] * i[2] #вес одного предмета * кол-во таких предметов
    return result

while True:
    user_in = input('Введите действие, которое необходимо выполнить (addItem, removeItem, showInventory, exit): ').lower()
    if (user_in == "additem"):
        name = input('\tВведите название нового предмета: '); weight = float(input('\tВес предмета: '))
        if (totalInventoryWeight() + weight <= maxWeight):
            if (duplicateItem(name, weight)):
                duplicateItem(name)[1] += 1 #если в инвентаре уже есть такой предмет, увеличиваем кол-во такого предмета на 1
            else:
                inventory.append([name, 1, weight])
            print("\t[DONE] Предмет", name, "добавлен в инветарь");
        else:
            print("\t[!] Добавление предмета невозможно: перегруз инвентаря!")
    elif (user_in == "removeitem"):
        name = input('\tВведите название удаляемого предмета: ')
        if (duplicateItem(name)):
            inventory.remove(duplicateItem(name))
            print("\t[DONE] Удаление предмета", name, " прошло успешно");
        else:
            print("\t[!] Предмет с таким названием отсутствует в инвентаре")
    elif (user_in == "showinventory"):
        if (len(inventory) > 0):
            maxLength = 0;
            for i in inventory:
                if (len(i[0]) > maxLength):
                    maxLength = len(i[0])

            print("%s%-8s%-6s" % ("Item Name".ljust(maxLength + 4), "Count", "Weight"))
            for item in inventory:
                print("%s%-8s%-6s" % (item[0].ljust(maxLength + 4), item[1], item[2]))
        else:
            print("Инвентарь пуст.")
    elif (user_in == "clearinventory"):
        inventory.clear()
    elif (user_in == "exit"):
        break;
    else:
        print("[!] Команда не распознана. Попробуйте ещё раз.")