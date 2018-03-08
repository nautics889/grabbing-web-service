from html.parser import HTMLParser
from urllib.request import urlopen

class LinkHTMLParser(HTMLParser):
    def __init__(self, site_name, *args, **kwargs):
        # создание списка ссылок
        self.links = []
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
        return '<br>'.join(sorted(self.links))

    # деструктор объекта
    def __del__(self):
        pass