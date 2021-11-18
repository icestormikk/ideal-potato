a,b = float(input('Введите первое число: ')), float(input('Введите второе число: '));
print(f'a + b == {a + b}\na - b == {a - b}\na * b == {a * b}\na ^ b == {a ** b}')

if (b == 0): print("[!] Операции a / b, a // b, a % b выполнить невозможно: число b равно нулю")
else: print(f'a / b == {a / b}\na % b == {a % b}\na // b == {a // b}');
