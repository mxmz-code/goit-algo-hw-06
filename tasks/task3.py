from modules.shortest_path_algorithms import dijkstra, bellman_ford, a_star
from modules.graph_operations import create_graph
from modules.logger import log_execution_time

def task3():
    """
    Завдання 3: Алгоритми для знаходження найкоротших шляхів (Dijkstra, Bellman-Ford, A*).
    Використовує алгоритми для пошуку найкоротших шляхів в графі.
    """
    print("Алгоритми для знаходження найкоротших шляхів (Dijkstra, Bellman-Ford, A*)...")
    G = create_graph()
    
    print("Результати Dijkstra:")
    result_dijkstra = dijkstra(G, 1)
    print(result_dijkstra)
    log_execution_time(f"Dijkstra результат: {result_dijkstra}")

    print("\nРезультати Bellman-Ford:")
    result_bellman_ford = bellman_ford(G, 1)
    print(result_bellman_ford)
    log_execution_time(f"Bellman-Ford результат: {result_bellman_ford}")

    print("\nРезультати A*: ")
    result_a_star = a_star(G, 1, 5, {node: 1 for node in G.nodes()})
    print(result_a_star)
    log_execution_time(f"A* результат: {result_a_star}")
