class Cdpr:
    def __init__(self, code, name, age, page):
        self._code = code
        self._name = name
        self._age = age
        self._page = page

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, value):
        self._page = value
