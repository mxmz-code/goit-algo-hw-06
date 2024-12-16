import time
from concurrent.futures import ThreadPoolExecutor

def optimize_performance(algorithm, G, start):
    """
    Оптимізація продуктивності через багатопоточність для великих графів.
    :param algorithm: Алгоритм для виконання (наприклад, dijkstra)
    :param G: граф
    :param start: початкова вершина
    """
    with ThreadPoolExecutor() as executor:
        future = executor.submit(algorithm, G, start)
        return future.result()

def measure_time(func, *args, **kwargs):
    """
    Вимірює час виконання алгоритму.
    :param func: функція, яку потрібно виміряти
    :param args: аргументи функції
    :param kwargs: ключові аргументи функції
    """
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    print(f"Час виконання {func.__name__}: {end_time - start_time:.5f} секунд")
    return result
