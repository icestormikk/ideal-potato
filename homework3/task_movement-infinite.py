print("Начальное положение персонажа: [0, 0]\nВведите направление движения (left/right/up/down):")
cur = [0, 0]
while True:
    dir = input()
    prev = [cur[0], cur[1]] #положение персонажа с предыдущего шага
    if (dir == "left"):
        cur[0] -= 1
    elif (dir == "right"):
        cur[0] += 1
    elif (dir == "down"):
        cur[1] -= 1
    elif (dir == "up"):
        cur[1] += 1
    else:
        if (dir != "stop"):
            print("[!] Не удалось распознать направление", dir)
        break
    print(prev, "->",cur)
