import cgi
import sqlite3

class SQLighter:

    def __init__(self, db):
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()

    def select_all(self):
        with self.connection:
            return self.cursor.execute("SELECT * FROM links").fetchall()

    def add_row(self, content):
        with self.connection:
            print(content)
            self.cursor.execute('INSERT INTO links VALUES (?)', (content,))
            print("successful added")

    def close(self):
        self.connection.close()

form = cgi.FieldStorage()
link = form.getfirst("get_link", "none")


print("Content-type: text/html\n")
print("hello")

print(link)

print("continue")

db_obj = SQLighter("links.db")
print(link)
db_obj.add_row(link)
db_obj.close()

print("end")