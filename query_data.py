import sqlite3

# Подключение к базе данных SQLite
conn = sqlite3.connect('movies.db')
cursor = conn.cursor()

# Выполнение запроса с условием фильтрации
cursor.execute('''
    SELECT title, release_date, vote_average
    FROM movies
    WHERE genres LIKE '%Action%'
''')
action_movies = cursor.fetchall()

# Закрытие соединения с базой данных
conn.close()

# Вывод результатов
for movie in action_movies:
    print(movie)
