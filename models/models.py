import sqlite3

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.close()

    def execute(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        self.conn.commit()

    def fetch_all(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        return self.cursor.fetchall()

    def fetch_one(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        return self.cursor.fetchone()

class Model:
    def __init__(self, table_name):
        self.table_name = table_name

    def create(self, **kwargs):
        columns = ', '.join(kwargs.keys())
        placeholders = ', '.join(['?'] * len(kwargs))
        query = f"INSERT INTO {self.table_name} ({columns}) VALUES ({placeholders})"
        values = tuple(kwargs.values())
        with Database('music.db') as db:
            db.execute(query, values)

    def get_all(self):
        query = f"SELECT * FROM {self.table_name}"
        with Database('music.db') as db:
            return db.fetch_all(query)

    def get_by_id(self, id):
        query = f"SELECT * FROM {self.table_name} WHERE id = ?"
        with Database('music.db') as db:
            return db.fetch_one(query, (id,))

    def delete(self, id):
        query = f"DELETE FROM {self.table_name} WHERE id = ?"
        with Database('music.db') as db:
            db.execute(query, (id,))

class Artiste(Model):
    def __init__(self):
        super().__init__('artistes')

    def create(self, name):
        super().create(name=name)

    def get_songs(self, artiste_id):
        query = "SELECT * FROM songs WHERE artiste_id = ?"
        with Database('music.db') as db:
            return db.fetch_all(query, (artiste_id,))

class Song(Model):
    def __init__(self):
        super().__init__('songs')

    def create(self, title, artiste_id):
        super().create(title=title, artiste_id=artiste_id)