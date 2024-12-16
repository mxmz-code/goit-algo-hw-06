import networkx as nx
import heapq

def dijkstra(G, start):
    """
    Алгоритм Дейкстри для знаходження найкоротших шляхів від початкової вершини до всіх інших.
    :param G: Граф
    :param start: Початкова вершина
    :return: Словник з найкоротшими відстанями від start до всіх інших вершин
    """
    if start not in G:
        raise ValueError(f"Вершина {start} відсутня в графі.")
    
    # Ініціалізація відстаней до всіх вершин як нескінченність
    dist = {node: float('inf') for node in G.nodes()}
    dist[start] = 0  # Відстань до стартової вершини дорівнює 0
    unvisited = list(G.nodes())

    while unvisited:
        # Знаходимо вершину з мінімальною відстанню
        min_node = None
        for node in unvisited:
            if min_node is None or dist[node] < dist[min_node]:
                min_node = node
        
        # Оновлюємо відстані для сусідів мінімальної вершини
        for neighbor in G.neighbors(min_node):
            weight = G[min_node][neighbor].get('weight', 1)
            new_dist = dist[min_node] + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
        
        unvisited.remove(min_node)

    return dist

def bellman_ford(G, start):
    """
    Алгоритм Беллмана-Форда для знаходження найкоротших шляхів в графах з від'ємними вагами ребер.
    :param G: Граф
    :param start: Початкова вершина
    :return: Словник з найкоротшими відстанями від start до всіх інших вершин
    """
    if start not in G:
        raise ValueError(f"Вершина {start} відсутня в графі.")
    
    dist = {node: float('inf') for node in G.nodes()}
    dist[start] = 0

    # Виконуємо відпочаток по всіх ребрах графа
    for _ in range(len(G.nodes()) - 1):
        for u, v in G.edges():
            weight = G[u][v].get('weight', 1)
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
    
    # Перевірка на наявність негативних циклів
    for u, v in G.edges():
        weight = G[u][v].get('weight', 1)
        if dist[u] + weight < dist[v]:
            raise ValueError("Граф містить негативний цикл.")
    
    return dist

def floyd_warshall(G):
    """
    Алгоритм Флойда-Уоршелла для знаходження всіх пар найкоротших шляхів.
    :param G: Граф
    :return: Словник з найкоротшими відстанями між усіма парами вершин
    """
    # Перевірка на від'ємні ваги
    for u, v in G.edges():
        weight = G[u][v].get('weight', 1)
        if weight <= 0:
            raise ValueError(f"Вес ребра ({u}, {v}) має бути позитивним.")
    
    return dict(nx.all_pairs_shortest_path_length(G))

def a_star(G, start, goal, heuristic):
    """
    Алгоритм A* для знаходження найкоротшого шляху між двома вершинами з урахуванням евристики.
    :param G: Граф
    :param start: Початкова вершина
    :param goal: Мета-вершина
    :param heuristic: Словник з евристичними значеннями для кожної вершини
    :return: Шлях від start до goal
    """
    if start not in G or goal not in G:
        raise ValueError(f"Вершини {start} або {goal} відсутні в графі.")
    
    if not all(h >= 0 for h in heuristic.values()):
        raise ValueError("Евристика повинна бути не від'ємною.")
    
    open_list = []
    heapq.heappush(open_list, (0 + heuristic[start], start))
    came_from = {}
    g_score = {node: float('inf') for node in G.nodes()}
    g_score[start] = 0
    
    while open_list:
        _, current = heapq.heappop(open_list)
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        for neighbor in G.neighbors(current):
            tentative_g_score = g_score[current] + G[current][neighbor].get('weight', 1)
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic[neighbor]
                heapq.heappush(open_list, (f_score, neighbor))

    return None
