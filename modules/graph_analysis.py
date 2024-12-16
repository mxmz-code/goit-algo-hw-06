import networkx as nx
import matplotlib.pyplot as plt

def visualize_graph(G):
    """
    Візуалізує граф з використанням matplotlib.
    :param G: граф
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
    plt.title("Візуалізація графа")
    plt.show()

def analyze_graph(G):
    """
    Виводить основні характеристики графа: кількість вершин, кількість ребер, ступінь вершин.
    :param G: граф
    """
    print(f"Кількість вершин: {G.number_of_nodes()}")
    print(f"Кількість ребер: {G.number_of_edges()}")
    print(f"Ступінь вершин: {dict(G.degree())}")
    
    # Аналіз центральності вершин
    centrality = nx.degree_centrality(G)
    print(f"Центральність вершин: {centrality}")
