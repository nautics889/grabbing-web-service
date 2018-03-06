import cgi
import sqlite3

from htmlscrabbing import LinkHTMLParser

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
link = 'https://soundcloud.com/ecstaticrecordings/b1-protect-the-revolution'

lp = LinkHTMLParser(link)

print("Content-type: text/html\n")
print("hello")

print(lp.get_links())



print(link)

print("continue")

db_obj = SQLighter("links.db")
print(link)
#db_obj.add_row(link, lp.get_links())
lp.__del__()
db_obj.close()

print("end")