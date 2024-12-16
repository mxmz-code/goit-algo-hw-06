import tkinter as tk
from tkinter import messagebox
from tkinter.simpledialog import askinteger
from modules.graph_operations import generate_random_graph, visualize_graph, analyze_graph
import networkx as nx
import matplotlib.pyplot as plt


class GraphGUI:
    def __init__(self, root, main_menu_callback):
        self.root = root
        self.root.title("Графічний інтерфейс для роботи з графами")
        self.main_menu_callback = main_menu_callback  # callback для повернення до головного меню
        
        self.label = tk.Label(root, text="Виберіть дію з графом:")
        self.label.pack(pady=10)
        
        # Кнопка для створення графа
        self.create_button = tk.Button(root, text="Створити граф", command=self.create_graph)
        self.create_button.pack(pady=5)
        
        # Кнопка для візуалізації графа
        self.visualize_button = tk.Button(root, text="Візуалізувати граф", command=self.visualize_graph)
        self.visualize_button.pack(pady=5)
        
        # Кнопка для аналізу графа
        self.analyze_button = tk.Button(root, text="Аналіз графа", command=self.analyze_graph)
        self.analyze_button.pack(pady=5)
        
        # Кнопка для виходу з GUI та повернення до головного меню
        self.quit_button = tk.Button(root, text="Вихід", command=self.quit_program)
        self.quit_button.pack(pady=5)

    def create_graph(self):
        """Запитує у користувача параметри та створює граф"""
        vertices = self.ask_for_vertices()
        if vertices is None:
            return
        
        edge_prob = self.ask_for_edge_probability()
        if edge_prob is None:
            return
        
        graph_type = self.select_graph_type()
        if graph_type is None:
            return
        
        # Генеруємо граф з вибраними параметрами
        self.graph = generate_random_graph(num_nodes=vertices, edge_prob=edge_prob, graph_type=graph_type)
        messagebox.showinfo("Інформація", "Граф успішно створений!")

    def ask_for_vertices(self):
        """Запитує у користувача кількість вершин"""
        vertices = askinteger("Вибір параметрів", "Введіть кількість вершин:")
        if vertices is None or vertices <= 0:
            messagebox.showerror("Помилка", "Введіть правильну кількість вершин.")
            return None
        return vertices

    def ask_for_edge_probability(self):
        """Запитує у користувача ймовірність зв'язку між вершинами"""
        edge_prob = askinteger("Вибір параметрів", "Введіть ймовірність зв'язку між вершинами (від 0 до 100):")
        if edge_prob is None or edge_prob < 0 or edge_prob > 100:
            messagebox.showerror("Помилка", "Введіть правильну ймовірність зв'язку (від 0 до 100).")
            return None
        return edge_prob / 100  # Перетворюємо в значення від 0 до 1

    def select_graph_type(self):
        """Запитує у користувача тип графа (орієнтований чи ні)"""
        answer = messagebox.askquestion("Тип графа", "Орієнтований граф? (Так/Ні)")
        if answer == 'yes':
            return 'directed'
        else:
            return 'undirected'

    def visualize_graph(self):
        """Візуалізує граф, якщо він створений"""
        if not hasattr(self, 'graph'):
            messagebox.showerror("Помилка", "Граф не створено. Спочатку створіть граф.")
            return
        visualize_graph(self.graph)

    def analyze_graph(self):
        """Аналізує граф, якщо він створений"""
        if not hasattr(self, 'graph'):
            messagebox.showerror("Помилка", "Граф не створено. Спочатку створіть граф.")
            return
        analyze_graph(self.graph)

    def quit_program(self):
        """Закриває GUI та повертає до головного меню"""
        response = messagebox.askyesno("Вихід", "Ви дійсно хочете повернутися до головного меню?")
        if response:
            self.root.quit()  # Закриває вікно Tkinter
            self.main_menu_callback()  # Повертає до головного меню


def run_gui(main_menu_callback):
    """Запускає GUI інтерфейс"""
    root = tk.Tk()
    app = GraphGUI(root, main_menu_callback)
    root.mainloop()
