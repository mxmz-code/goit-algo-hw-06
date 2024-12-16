import networkx as nx
import random
import matplotlib.pyplot as plt

def create_graph(graph_type='undirected'):
    """
    Створює граф з заданим типом.
    Типи графів:
    - 'undirected' (за замовчуванням) — неорієнтований граф
    - 'directed' — орієнтований граф
    :param graph_type: Тип графа
    :return: Граф
    """
    if graph_type not in ['undirected', 'directed']:
        raise ValueError("Невірний тип графа! Використовуйте 'undirected' або 'directed'.")
    
    # Створюємо граф в залежності від типу
    if graph_type == 'directed':
        G = nx.DiGraph()
    else:
        G = nx.Graph()
    
    # Додавання вершин і ребер
    G.add_nodes_from([1, 2, 3, 4, 5, 6])
    G.add_edge(1, 2, weight=3)
    G.add_edge(2, 3, weight=2)
    G.add_edge(3, 4, weight=1)
    G.add_edge(4, 5, weight=4)
    G.add_edge(5, 6, weight=2)
    G.add_edge(6, 1, weight=3)
    
    return G

def generate_random_graph(num_nodes=10, edge_prob=0.3, graph_type='undirected'):
    """
    Генерація випадкового графа з заданими параметрами.
    :param num_nodes: Кількість вершин
    :param edge_prob: Ймовірність наявності ребра між двома вершинами
    :param graph_type: Тип графа ('undirected' або 'directed')
    :return: Випадковий граф
    """
    if not isinstance(num_nodes, int) or num_nodes <= 0:
        raise ValueError("Число вершин повинно бути цілим додатним числом.")
    
    if not (0 <= edge_prob <= 1):
        raise ValueError("Ймовірність повинна бути в межах [0, 1].")
    
    if graph_type not in ['undirected', 'directed']:
        raise ValueError("Невірний тип графа! Використовуйте 'undirected' або 'directed'.")
    
    # Генерація випадкового графа
    if graph_type == 'directed':
        G = nx.erdos_renyi_graph(num_nodes, edge_prob, directed=True)
    else:
        G = nx.erdos_renyi_graph(num_nodes, edge_prob)
    
    # Додавання випадкових ваг на ребра
    for (u, v) in G.edges():
        G[u][v]['weight'] = random.randint(1, 10)
    
    return G

def visualize_graph(G):
    """
    Візуалізація графа.
    :param G: Граф для візуалізації
    """
    if not isinstance(G, nx.Graph):
        raise TypeError("Очікується об'єкт типу networkx.Graph.")
    
    # Розташування вершин у графі для візуалізації
    pos = nx.spring_layout(G)
    
    # Малюємо граф
    nx.draw(G, pos, with_labels=True, node_color='lightblue', font_weight='bold', node_size=3000)
    
    # Додаємо етикетки до ребер (ваги)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
    # Заголовок
    plt.title("Граф")
    plt.show()

def analyze_graph(G):
    """
    Аналіз характеристик графа.
    Виводить кількість вершин, кількість ребер і ступінь кожної вершини.
    :param G: Граф для аналізу
    """
    if not isinstance(G, nx.Graph):
        raise TypeError("Очікується об'єкт типу networkx.Graph.")
    
    # Виводимо характеристики графа
    print(f"Кількість вершин: {G.number_of_nodes()}")
    print(f"Кількість ребер: {G.number_of_edges()}")
    print(f"Ступінь вершин: {dict(G.degree())}")
