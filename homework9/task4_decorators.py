import random
import time
import logging

logger = logging.getLogger("function_logger")
logger.setLevel(logging.INFO)

fh = logging.FileHandler("logs.txt")
fh.setFormatter(
    logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    )
logger.addHandler(fh)

def log_decorator(func):
    def wrapper(matr):
        logger.info(f'Function {func.__name__} has been started')
        try:
            func(matr)
        except Exception as e:
            logger.exception(f'Function {func.__name__} failed: {e}')
        else:
            logger.info(f'Function {func.__name__} finished')
    return wrapper

def time_decorator(func):
    def wrapper(matr):
        start_time = time.time()
        try:
            func(matr)
        except Exception as e:
            print(f'Function {func.__name__} failed: {e}')
        else:
            print("Execution time of the \"%s\" function: %f sec"
                % (func.__name__, time.time() - start_time))
    return wrapper

def stop_decorator(func):
    def wrapper(matr):
        try:
            func(matr)
        except Exception as e:
            print(f'Function {func.__name__} failed: {e}')
        else:
            print(f'Execution of {func.__name__} function stopped by 5 sec')
            time.sleep(5)
    return wrapper

#@log_decorator
@time_decorator
#@stop_decorator
def gauss(matr):
    """
    Прямой ход метода Гаусса.

    Функция приводит квадратную n * n матрицу к верхнему треугольному виду
    (не сокращая элементы, стоящие на главной диагонали).
    
    Аргументы:
    matr - двумерный массив размером N * N
    """

    for i in matr:
        if (len(matr) != len(i)):
            raise ValueError('The matrix is not square.')

    for i in range(len(matr)):
        if (matr[i][i] == 0): continue
        for j in range(i + 1, len(matr[i])):
            c = matr[j][i] / matr[i][i]
            for k in range(i, len(matr[i])):
                matr[j][k] -= c * matr[i][k]
    return matr

SIZE = 100
gauss([[random.randint(1,10) for i in range(SIZE)] for i in range(SIZE)])