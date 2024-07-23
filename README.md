# Movie Database Project

Это проект по работе с базой данных фильмов и визуализацией данных. Проект состоит из нескольких шагов: создание базы данных, импорт данных, написание SQL-запросов и визуализация результатов.

## Содержание

- `import_data.py` - скрипт для создания базы данных и импорта данных из CSV файлов.
- `query_data.py` - пример SQL-запроса для извлечения данных о фильмах жанра "Action".
- `average_rating.py` - скрипт для расчета среднего рейтинга фильмов.
- `genre_count_barplot.py` - скрипт для построения диаграммы количества фильмов в каждом жанре.
- `tmdb_5000_movies.csv` - исходный файл с данными о фильмах.
- `tmdb_5000_credits.csv` - исходный файл с данными о кредитах.

## Установка

1. Клонируйте репозиторий:
    ```sh
    git clone https://github.com/Sablinanton/movie-database-project.git
    cd movie-database-project
    ```

2. Установите необходимые зависимости:
    ```sh
    pip install pandas sqlite3 matplotlib seaborn
    ```

## Использование

1. Запустите `import_data.py` для создания базы данных и импорта данных:
    ```sh
    python import_data.py
    ```

2. Запустите `query_data.py` для выполнения SQL-запроса и извлечения данных о фильмах жанра "Action":
    ```sh
    python query_data.py
    ```

3. Запустите `average_rating.py` для расчета среднего рейтинга фильмов:
    ```sh
    python average_rating.py
    ```

4. Запустите `genre_count_barplot.py` для построения диаграммы количества фильмов в каждом жанре:
    ```sh
    python genre_count_barplot.py
    ```
## Графики

### Распределение рейтингов фильмов
![Распределение рейтингов фильмов](./ratings_histogram.png)

### Количество фильмов в каждом жанре
![Количество фильмов в каждом жанре](./genre_count_barplot.png)
