import cgi
import sqlite3

from htmlgrabbing import LinkHTMLParser

'''Подключение к БД'''
class SQLighter:

    def __init__(self, db):
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()

    def select_all(self):
        with self.connection:
            return self.cursor.execute("SELECT * FROM links").fetchall()

    def add_row(self, link, content):
        with self.connection:
            self.cursor.execute('INSERT INTO links VALUES (?, ?)', (link, content))
            print("successful added")

    def close(self):
        self.connection.close()

'''Обработка строк'''
form = cgi.FieldStorage()
link = form.getfirst("get_link", "none")

print(link)

lp = LinkHTMLParser(link)

print("Content-type: text/html\n")
print("hello")

print(lp.get_links())

with open('output.txt', 'w') as f:
    f.write(lp.get_links())

print(link)

print("continue")

db_obj = SQLighter("links.db")

db_obj.add_row(link, lp.get_links())

db_obj.close()

lp.__del__()

print("end")