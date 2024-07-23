import sqlite3
import pandas as pd

# Подключение к базе данных SQLite (или её создание)
conn = sqlite3.connect('movies.db')

# Создание объекта курсора
cursor = conn.cursor()

# Удаление существующих таблиц для перезапуска
cursor.execute('DROP TABLE IF EXISTS movies')
cursor.execute('DROP TABLE IF EXISTS credits')

# Создание таблиц в базе данных с учетом всех столбцов
cursor.execute('''
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY,
        title TEXT,
        budget INTEGER,
        revenue INTEGER,
        original_language TEXT,
        release_date TEXT,
        vote_average REAL,
        vote_count INTEGER,
        overview TEXT,
        popularity REAL,
        runtime INTEGER,
        tagline TEXT,
        status TEXT,
        production_companies TEXT,
        production_countries TEXT,
        genres TEXT,
        homepage TEXT,
        keywords TEXT,
        original_title TEXT,
        spoken_languages TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS credits (
        id INTEGER PRIMARY KEY,
        movie_id INTEGER,
        title TEXT,
        cast TEXT,
        crew TEXT
    )
''')

# Сохранение изменений
conn.commit()

# Загрузка данных из CSV файлов
movies_data = pd.read_csv('C:\\Users\\DELTA\\Desktop\\DS\\дз 23.07\\tmdb_5000_movies.csv')
credits_data = pd.read_csv('C:\\Users\\DELTA\\Desktop\\DS\\дз 23.07\\tmdb_5000_credits.csv')

# Импорт данных в таблицу movies
movies_data.to_sql('movies', conn, if_exists='append', index=False)

# Импорт данных в таблицу credits
credits_data.to_sql('credits', conn, if_exists='append', index=False)

# Закрытие соединения с базой данных
conn.close()
