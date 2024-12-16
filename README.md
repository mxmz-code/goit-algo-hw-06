
# Домашнє завдання: Графи (goit-algo-hw-06)

Це домашнє завдання стосується роботи з графами та реалізації основних алгоритмів для пошуку шляхів у графах, таких як пошук в глибину (DFS), пошук в ширину (BFS) та алгоритм Дейкстри для знаходження найкоротшого шляху. Для виконання завдання ми використали бібліотеку `networkX` в Python.

## Опис завдань

### Завдання 1: Створення графа

Ми повинні були створити граф, який моделює реальну мережу, наприклад, транспортну мережу міста чи соціальну мережу. Для цього використовували бібліотеку `networkX`, яка дозволяє зручно працювати з графами в Python.

1. **Створення графа:** Ми створили порожній граф, додавши вершини і ребра для моделювання конкретної мережі.
2. **Аналіз графа:** Після створення графа, ми проаналізували основні характеристики: кількість вершин, кількість ребер та ступінь кожної вершини.
3. **Візуалізація:** Для наочності вивели граф за допомогою `matplotlib`, щоб побачити його структуру.

**Код:**
```python
import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (1, 4)])

# Візуалізація
nx.draw(G, with_labels=True)
plt.show()

# Аналіз характеристик
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degrees = dict(G.degree())

print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print(f"Ступені вершин: {degrees}")
```

### Завдання 2: Пошук шляхів з використанням DFS і BFS

У цьому завданні ми повинні були реалізувати два основні алгоритми пошуку шляхів у графі:

1. **DFS (Пошук в глибину):** Алгоритм, який працює шляхом обходу графа через його гілки.
2. **BFS (Пошук в ширину):** Алгоритм, який обходить граф рівнями, знаходячи найкоротший шлях від початкової вершини.

Після реалізації кожного з алгоритмів ми порівняли отримані результати для шляху між двома вершинами, з'ясувавши, чому ці шляхи відрізняються.

**Код для DFS і BFS:**
```python
# Пошук в глибину (DFS)
def dfs(graph, start):
    visited = set()
    stack = [start]
    path = []
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            path.append(vertex)
            stack.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)
    return path

# Пошук в ширину (BFS)
def bfs(graph, start):
    visited = set()
    queue = [start]
    path = []
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            path.append(vertex)
            queue.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)
    return path

graph = {1: [2, 4], 2: [1, 3], 3: [2, 4], 4: [1, 3]}
print("DFS:", dfs(graph, 1))
print("BFS:", bfs(graph, 1))
```

### Завдання 3: Алгоритм Дейкстри для пошуку найкоротшого шляху

У цьому завданні ми реалізували алгоритм Дейкстри, який дозволяє знайти найкоротший шлях між усіма вершинами графа, враховуючи ваги на ребрах. Алгоритм працює, поступово знаходячи мінімальні відстані від початкової вершини до всіх інших.

1. **Додавання ваги до ребер:** Ваги додаються до ребер для моделювання реальних відстаней чи вартостей.
2. **Реалізація алгоритму Дейкстри:** Алгоритм Дейкстри використовується для обчислення найкоротших шляхів від початкової вершини до всіх інших.

**Код:**
```python
import heapq

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Приклад графа з вагами
graph = {
    1: {2: 1, 4: 3},
    2: {1: 1, 3: 1},
    3: {2: 1, 4: 1},
    4: {1: 3, 3: 1}
}
print(dijkstra(graph, 1))
```
