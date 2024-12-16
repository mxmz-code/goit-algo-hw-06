import time
import os
from modules.logger import log_execution_time
from modules.performance import measure_time, optimize_performance
from modules.gui import run_gui  # Імпортуємо функцію для запуску GUI
from tasks.task1 import task1  # Імпортуємо task1 з папки tasks
from tasks.task2 import task2  # Імпортуємо task2 з папки tasks
from tasks.task3 import task3  # Імпортуємо task3 з папки tasks
from modules.graph_operations import generate_random_graph  # Додано імпорт функції для генерації графа
from modules.shortest_path_algorithms import dijkstra, bellman_ford, a_star  # Додано імпорт алгоритмів для пошуку найкоротших шляхів


def clear_screen():
    """Очищає екран"""
    if os.name == 'nt':  # Для Windows
        os.system('cls')
    else:  # Для Linux/Mac
        os.system('clear')


def performance_test():
    """
    Функція для тестування продуктивності різних алгоритмів.
    Виводить час виконання для алгоритмів Dijkstra, Bellman-Ford та A*.
    Тестуємо на більших графах для чіткішого вимірювання часу виконання.
    """
    clear_screen()
    print("Тестування продуктивності алгоритмів...")
    
    # Збільшуємо кількість вершин і ймовірність для ребер, щоб зробити граф більшим
    num_nodes = 1000  # Збільшено кількість вершин
    edge_prob = 0.05  # Збільшена ймовірність для більшої щільності графа

    # Створюємо великий випадковий граф
    G = generate_random_graph(num_nodes=num_nodes, edge_prob=edge_prob, graph_type='undirected')

    # Тестування Dijkstra
    start_time = time.time()
    dijkstra(G, 1)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Час виконання Dijkstra: {execution_time:.5f} секунд")
    log_execution_time(f"Dijkstra виконано за {execution_time:.5f} секунд")  # Логуємо результат

    # Тестування Bellman-Ford
    start_time = time.time()
    bellman_ford(G, 1)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Час виконання Bellman-Ford: {execution_time:.5f} секунд")
    log_execution_time(f"Bellman-Ford виконано за {execution_time:.5f} секунд")  # Логуємо результат

    # Тестування A*
    start_time = time.time()
    a_star(G, 1, 100, {node: 1 for node in G.nodes()})  # Використовуємо більшу мету для A*
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Час виконання A*: {execution_time:.5f} секунд")
    log_execution_time(f"A* виконано за {execution_time:.5f} секунд")  # Логуємо результат


def menu():
    """
    Меню для вибору задачі.
    Користувач може вибрати одну з доступних задач.
    """
    while True:
        clear_screen()
        print("Виберіть задачу:")
        print("1. Створення графа і його аналіз через GUI")
        print("2. Пошук шляхів (DFS, BFS)")
        print("3. Алгоритми для знаходження найкоротших шляхів (Dijkstra, Bellman-Ford, A*)")
        print("4. Тестування продуктивності")
        print("5. Вихід")
        
        # Зчитуємо вибір користувача
        choice = input("Введіть номер задачі: ")

        if choice == "1":
            # Завдання 1: створення графа через GUI
            run_gui(menu)  # Запуск графічного інтерфейсу
            continue_option()
        
        elif choice == "2":
            # Завдання 2: пошук шляхів за допомогою BFS і DFS
            task2()
            continue_option()

        elif choice == "3":
            # Завдання 3: алгоритми для знаходження найкоротших шляхів
            task3()
            continue_option()

        elif choice == "4":
            # Тестування продуктивності
            performance_test()
            continue_option()

        elif choice == "5":
            print("Вихід з програми.")
            break  # Завершує програму

        else:
            print("Невірний вибір. Спробуйте ще раз.")
            time.sleep(2)  # Затримка перед поверненням до меню


def continue_option():
    """
    Запитує у користувача, чи хоче він продовжити чи вийти з програми.
    """
    while True:
        choice = input("\nЩо ви хочете зробити далі?\n1. Продовжити\n2. Вийти\nВведіть номер: ")
        
        if choice == "1":
            return  # Продовжує поточний процес
        elif choice == "2":
            print("Вихід з програми.")
            break  # Завершує програму
        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    menu()
