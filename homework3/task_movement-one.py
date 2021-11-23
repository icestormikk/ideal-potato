print("Начальное положение персонажа: [0, 0]");
dir = input('Введите направление движения (left/right/up/down): '); pos = [0, 0];
if (dir == "left"):
    pos[0] -= 1;
elif (dir == "right"):
    pos[0] += 1;
elif (dir == "down"):
    pos[1] -= 1;
elif (dir == "up"):
    pos[1] += 1;
else:
    print("[!] Не удалось распознать направление", dir);
    exit();

print("Новое положение персонажа:", pos);
