import logging
import os

# Створюємо логер
logger = logging.getLogger()
logger.setLevel(logging.INFO)  # Встановлюємо рівень логування

# Створюємо обробник для запису логів у файл
log_file_path = os.path.join(os.getcwd(), 'logs', 'app.log')

# Якщо директорія для логів не існує, створюємо її
if not os.path.exists(os.path.dirname(log_file_path)):
    os.makedirs(os.path.dirname(log_file_path))

file_handler = logging.FileHandler(log_file_path)
file_handler.setLevel(logging.INFO)  # Рівень логування для цього обробника

# Формат для логів
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Додаємо обробник до логера
logger.addHandler(file_handler)

def log_execution_time(message):
    """Функція для запису часу виконання"""
    logger.info(message)
