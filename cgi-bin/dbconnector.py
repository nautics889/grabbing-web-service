# -*- coding: utf-8 -*-
import sqlite3

class SQLighter:

    def __init__(self, db):
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()

    def select_all(self):
        with self.connection:
            return self.cursor.execute("SELECT * FROM links").fetchall()

    def add_row(self, content):
        self.execute('INSERT INTO links VALUES (?)', content)

    def close(self):
        self.connection.close()