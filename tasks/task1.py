from modules.graph_operations import generate_random_graph, visualize_graph, analyze_graph

def task1():
    """
    Завдання 1: Створення графа, його візуалізація та аналіз.
    Використовує функції для створення випадкового графа, візуалізації та аналізу його характеристик.
    """
    print("Створення графа і його аналіз...")
    # Параметри графа
    num_nodes = 10  # Кількість вершин
    edge_prob = 0.3  # Ймовірність для ребер

    # Створення графа
    G = generate_random_graph(num_nodes=num_nodes, edge_prob=edge_prob, graph_type='undirected')

    # Візуалізація графа
    visualize_graph(G)

    # Аналіз характеристик графа
    analyze_graph(G)
