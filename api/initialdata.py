import sqlite3

def initialize_database():
    conn = sqlite3.connect('movies.db')
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            year INTEGER NOT NULL
        )

    ''')
    cur.executemany('''
        INSERT INTO movies (id, title, year) VALUES (?, ?, ?)
    ''', [
        (1, 'Inception', 2010),
        (2, '3 Idiots', 2009),
        (3, 'Enthiran', 2010),
        (4, 'The Dark Knight', 2008),
        (5, 'Dangal', 2016),
        (6, 'Bahubali: The Beginning', 2015),
        (7, 'Vikram', 2022),
        (8, 'Titanic', 1997),
        (9, 'Gully Boy', 2019),
        (10, 'Master', 2021)
    ])

    cur.execute('''
                 CREATE TABLE IF NOT EXISTS actors (
                     id INTEGER PRIMARY KEY,
                     name TEXT NOT NULL,
                     birth_year INTEGER NOT NULL
                 )
                 ''')
    cur.executemany('''
                 INSERT INTO actors (id, name, birth_year) VALUES (?, ?, ?)
                 ''', [
                        (1, 'Leonardo DiCaprio', 1974),
                        (2, 'Aamir Khan', 1965),
                        (3, 'R. Madhavan', 1970),
                        (4, 'Rajinikanth', 1950),
                        (5, 'Christian Bale', 1974),
                        (6, 'Heath Ledger', 1979),
                        (7, 'Fatima Sana Shaikh', 1992),
                        (8, 'Prabhas', 1979),
                        (9, 'Kamal Haasan', 1954),
                        (10, 'Kate Winslet', 1975),
                        (11, 'Ranveer Singh', 1985),
                        (12, 'Vijay Sethupathi', 1978),
                        (13, 'Anne Hathaway', 1982),
                        (14, 'Sharman Joshi', 1979),
                        (15, 'Anushka Shetty', 1981),
                        (16, 'Vijay', 1974)
                 ])
    cur.execute('''
                CREATE TABLE IF NOT EXISTS directors (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    birth_year INTEGER NOT NULL
                )
                ''')
    cur.executemany('''
                INSERT INTO directors (id, name, birth_year) VALUES (?, ?, ?)
                ''', [
                    (1, 'Christopher Nolan', 1970),
                    (2, 'Rajkumar Hirani', 1962),
                    (3, 'S. Shankar', 1963),
                    (4, 'Nitesh Tiwari', 1973),
                    (5, 'S. S. Rajamouli', 1973),
                    (6, 'Lokesh Kanagaraj', 1986),
                    (7, 'James Cameron', 1954),
                    (8, 'Zoya Akhtar', 1972)
                ])
    cur.execute('''
                CREATE TABLE IF NOT EXISTS genres (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL
                )
                ''')
    cur.executemany('''
                INSERT INTO genres (id, name) VALUES (?, ?)
                ''', [
                    (1, 'Sci-Fi'),
                    (2, 'Thriller'),
                    (3, 'Action'),
                    (4, 'Crime'),
                    (5, 'Comedy'),
                    (6, 'Drama'),
                    (7, 'Romance'),
                    (8, 'Historical'),
                    (9, 'Musical'),
                    (10, 'Fantasy')
                ])
    cur.execute('''
                CREATE TABLE IF NOT EXISTS movie_genres (
                    movie_id INTEGER,
                    genre_id INTEGER,
                    PRIMARY KEY (movie_id, genre_id),
                    FOREIGN KEY (movie_id) REFERENCES movies (id),
                    FOREIGN KEY (genre_id) REFERENCES genres (id)
                )
                ''')
    cur.executemany('''
                INSERT INTO movie_genres (movie_id, genre_id) VALUES (?, ?)
                ''', [
                        (1, 1), (1, 2),
                        (2, 5), (2, 6),
                        (3, 1), (3, 3),
                        (4, 3), (4, 4),
                        (5, 6),
                        (6, 3), (6, 10),
                        (7, 2), (7, 3),
                        (8, 6), (8, 7),
                        (9, 6), (9, 9),
                        (10, 2), (10, 3)
                ])
    
    cur.execute('''
                CREATE TABLE IF NOT EXISTS movie_actors (
                    movie_id INTEGER,
                    actor_id INTEGER,
                    PRIMARY KEY (movie_id, actor_id),
                    FOREIGN KEY (movie_id) REFERENCES movies (id),
                    FOREIGN KEY (actor_id) REFERENCES actors (id)
                )
                ''')
    cur.executemany('''
                INSERT INTO movie_actors (movie_id, actor_id) VALUES (?, ?)
                ''', [
                        (1, 1),
                        (1, 13),
                        (2, 2),
                        (2, 3),
                        (2, 14),
                        (3, 4),
                        (4, 5),
                        (4, 6),
                        (5, 2),
                        (5, 7),
                        (6, 8),
                        (6, 15),
                        (7, 9),
                        (7, 12),
                        (8, 1),
                        (8, 10),
                        (9, 11),
                        (10, 16),
                        (10, 12)
                ])
    
    cur.execute('''
                CREATE TABLE IF NOT EXISTS movie_directors (
                    movie_id INTEGER,
                    director_id INTEGER,
                    PRIMARY KEY (movie_id, director_id),
                    FOREIGN KEY (movie_id) REFERENCES movies (id),
                    FOREIGN KEY (director_id) REFERENCES directors (id)
                )
                ''')
    cur.executemany('''
                INSERT INTO movie_directors (movie_id, director_id) VALUES (?, ?)
                ''', [
                        (1, 1),
                        (2, 2),
                        (3, 3),
                        (4, 1),
                        (5, 4),
                        (6, 5),
                        (7, 6),
                        (8, 7),
                        (9, 8),
                        (10, 6)
                ])
    
    

    conn.commit()
    conn.close()



if __name__ == "__main__":
    initialize_database()