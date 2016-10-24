class Person(object):
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

    def getname(self):
        return self.name

    def getlastname(self):
        return self.lastname

    def setname(self, name):
        self.name = name

    def setlastname(self, lastname):
        self.lastname = lastname

person = Person('Rolando', 'Villca')

def changed():
    return 'Patched method!!!'

def test(person):
    print person.getname()
    person.setname('Rolando222')
    
    print person.getname()
    print

    person.getname = changed
    print person.getname()

test(person)