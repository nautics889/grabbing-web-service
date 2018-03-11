import cgi

from htmlgrabbing import WebHTMLParser
from databaseconnector import SQLighter

'''Обработка строк'''
form = cgi.FieldStorage()
link = form.getfirst("get_link", "none")

lp = WebHTMLParser(link)

print("Content-type: text/html\n")
print(lp.get_mails())

db_obj = SQLighter("links.db")

db_obj.add_row_mails(link, lp.get_mails())

db_obj.close()

lp.__del__()