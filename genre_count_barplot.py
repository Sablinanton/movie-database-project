import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import ast

# Подключение к базе данных SQLite
conn = sqlite3.connect('movies.db')

# Загрузка данных из таблицы movies
movies_data = pd.read_sql_query('SELECT genres FROM movies', conn)

# Закрытие соединения с базой данных
conn.close()

# Преобразование строковых представлений списка жанров в список
def extract_genres(genres_str):
    genres = ast.literal_eval(genres_str)
    return [genre['name'] for genre in genres]

movies_data['genres_list'] = movies_data['genres'].apply(extract_genres)

# Разворачивание списка жанров в одну колонку
all_genres = movies_data.explode('genres_list')

# Подсчет количества фильмов в каждом жанре
genre_counts = all_genres['genres_list'].value_counts()

# Построение диаграммы количества фильмов в каждом жанре
sns.barplot(x=genre_counts.values, y=genre_counts.index)
plt.title('Количество фильмов в каждом жанре')
plt.xlabel('Количество фильмов')
plt.ylabel('Жанр')
plt.show()
