fib_values = {0: 0, 1: 1}
def fibonacci(n):
    if (n in fib_values):
        return fib_values[n]
    else:
        if (n > 0):
            fib_values[n] = fibonacci(n - 1) + fibonacci(n - 2)
        else:
            fib_values[n] = fibonacci(n + 2) - fibonacci(n + 1)
        return fib_values[n]

try:
    print("Искомое число Фибоначчи:", fibonacci(int(input('Введите индекс числа Фибоначчи: '))));
except ValueError:
    print("[!] Ошибка ввода (требуется одно целое число)")