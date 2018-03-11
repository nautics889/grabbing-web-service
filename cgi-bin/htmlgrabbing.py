from html.parser import HTMLParser
from urllib.request import urlopen

import re

class WebHTMLParser(HTMLParser):
    def __init__(self, site_name, *args, **kwargs):
        # создание списка ссылок
        self.links = []
        # создание списка телефонных номеров
        self.numbers = []
        # регулярное выражение для поиска телефонных номеров
        self.numbersRegex = re.compile(r'\+38\s?\(\d{3}\)\s?\d{3}-?\d{2}-?\d{2}')
        # создание списка e-mail адресов
        self.mails = []
        # регулярное выражение для поиска почтовых адресов
        self.mailsRegex = re.compile(r'[-.\w]+@(?:[a-z\d]{2,}\.)+[a-z]{2,6}')
        # инициализация имени сайта
        self.site_name = site_name
        # вызыв конктруктора родителя
        super().__init__(*args, **kwargs)
        # считывание контента веб-страницы
        self.feed(self.read_site_content())

    def handle_starttag(self, tag, attrs):
        # проверка является ли тэг тэгом ссылки
        if tag == 'a':
            # поиск атрибута адреса ссылки
            for attr in attrs:
                if attr[0] == 'href':
                    if not self.validate(attr[0]):
                        # добавление в список ссылок
                        if self.validate_link(attr[1]):
                            self.links.append(attr[1])

    def get_phones(self):
        self.numbers = self.numbersRegex.findall(self.read_site_content())
        if (len(self.numbers)!=0):
            return '<br>'.join(sorted(set(self.numbers)))
        else:
            return 'No numbers was found.'

    def get_mails(self):
        self.mails = self.mailsRegex.findall(self.read_site_content())
        if (len(self.mails)!=0):
            return '<br>'.join(sorted(set(self.mails)))
        else:
            return 'No e-mails was found.'

    def validate(self, link):
        """ Функция проверяет стоит ли добавлять ссылку в список адресов.
        В список адресов стоит добавлять если ссылка:
             1) Еще не в списке ссылок
             2) Не вызывает javascript-код
             3) Не ведет к какой-либо метке. (Не содержит #)
         """
        if link[0]=='/':
            return True
        return link in self.links or '#' in link or 'javascript:' in link

    def validate_link(self, link):
        """
        Дополнительная валидация:
        ссылка будет добавлена, если она начинается с http.
        Это позволяет избавится от локальных ссылок
        """
        if link[:4]=='http':
            return True
        else:
            False

    # считывание контента
    def read_site_content(self):
        return str(urlopen(self.site_name).read())

    # метод для получения готового списка
    def get_links(self):
        if (len(self.links)!=0):
            return '<br>'.join(sorted(self.links))
        else:
            return 'No links was found.'

    # деструктор объекта
    def __del__(self):
        pass