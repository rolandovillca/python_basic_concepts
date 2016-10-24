country = 'Bolivia'

def get_country():
    return country

def set_country(country=None):
    country = country
    print 'Country was set'

class Person(object):
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

    def get_name(self):
        return self.name

    def get_lastname(self):
        return self.lastname

    def set_name(self, name):
        self.name = name

    def set_lastname(self, lastname):
        self.lastname = lastname