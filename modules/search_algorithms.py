import networkx as nx
from collections import deque

def bfs(graph, start, goal):
    """
    Алгоритм пошуку в ширину (BFS) для знаходження найкоротшого шляху між вершинами.
    BFS працює шляхом відвідування всіх суміжних вершин з початкової, поступово рухаючись до глибинних рівнів.

    :param graph: Граф, на якому проводиться пошук.
    :param start: Вершина початку.
    :param goal: Вершина кінця.
    :return: Список вершин, що складають найкоротший шлях між start і goal.
    """
    print("\nАлгоритм BFS (Breadth-First Search) знаходить шлях, проходячи через усі суміжні вершини по черзі, починаючи з початкової.")
    print("Цей алгоритм гарантує, що він знайде найкоротший шлях за кількістю ребер у незважених графах.")

    # Ініціалізуємо чергу для відвідуваних вершин
    queue = deque([start])
    visited = set([start])  # Множина відвіданих вершин
    parent = {start: None}  # Словник для зберігання попередників вершин

    while queue:
        current = queue.popleft()

        # Якщо ми досягли кінцевої вершини, будуємо шлях
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]  # Повертаємо шлях у зворотному порядку

        # Додаємо всі суміжні вершини в чергу
        for neighbor in graph.neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

    return []  # Повертаємо порожній список, якщо шляху не знайдено


def dfs(graph, start, goal):
    """
    Алгоритм пошуку в глибину (DFS) для знаходження шляху між вершинами.
    DFS працює шляхом дослідження глибини кожної вершини перед тим, як перейти до наступної.

    :param graph: Граф, на якому проводиться пошук.
    :param start: Вершина початку.
    :param goal: Вершина кінця.
    :return: Список вершин, що складають шлях між start і goal.
    """
    print("\nАлгоритм DFS (Depth-First Search) працює, досліджуючи глибину кожної вершини перед тим, як перейти до наступної.")
    print("Цей алгоритм може знайти шлях, але не гарантує найкоротший шлях у графі.")

    # Стек для DFS
    stack = [start]
    visited = set([start])
    parent = {start: None}  # Словник для зберігання попередників вершин

    while stack:
        current = stack.pop()

        # Якщо ми досягли кінцевої вершини, будуємо шлях
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]  # Повертаємо шлях у зворотному порядку

        # Додаємо всі сусідні вершини в стек
        for neighbor in graph.neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                stack.append(neighbor)

    return []  # Повертаємо порожній список, якщо шляху не знайдено
