import sqlite3

# Подключение к базе данных SQLite
conn = sqlite3.connect('movies.db')
cursor = conn.cursor()

# Выполнение запроса для получения среднего рейтинга фильмов
cursor.execute('SELECT AVG(vote_average) FROM movies')
average_rating = cursor.fetchone()[0]

# Закрытие соединения с базой данных
conn.close()

# Вывод результата
print('Средний рейтинг фильмов:', average_rating)
