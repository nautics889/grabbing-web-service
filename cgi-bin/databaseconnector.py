import sqlite3
'''Подключение к БД'''
class SQLighter:

    def __init__(self, db):
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()

    def select_all(self):
        # взятие всех данных из таблицы
        with self.connection:
            return self.cursor.execute("SELECT * FROM links").fetchall()

    def add_row_links(self, link, content):
        # добавление результата в таблицу ссылок
        with self.connection:
            self.cursor.execute('INSERT INTO links VALUES (?, ?)', (link, content))

    def add_row_phones(self, link, content):
        # добавление результата в таблицу телефонных номеров
        with self.connection:
            self.cursor.execute('INSERT INTO numbers VALUES (?, ?)', (link, content))

    def add_row_mails(self, link, content):
        # добавление результата в таблицу почтовых адресов
        with self.connection:
            self.cursor.execute('INSERT INTO mails VALUES (?, ?)', (link, content))

    def close(self):
        # закрытие соединения с БД
        self.connection.close()