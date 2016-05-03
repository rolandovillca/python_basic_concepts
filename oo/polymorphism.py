# EXAMPLE 1: Polymorphism in Python with a function:
# ==============================================================================
# We create two classes:  Bear and Dog, both  can make a distinct sound.
# We then make two instances and call their action using the same method.

class Bear(object):
    def sound(self):
        print 'Groarrr'

class Dog(object):
    def sound(self):
        print 'Woof woof!'

def makeSound(animalType):
    animalType.sound()

bear_obj = Bear()
dog_obj = Dog()

makeSound(bear_obj)
makeSound(dog_obj)
print


# EXAMPLE 2: Polymorphism with abstract class (most commonly used):
# ==============================================================================
class Document:
    def __init__(self, name):
        self.name = name

    def show(self):
        raise NotImplementedError('Subclass must implement abstract method')

class Pdf(Document):
    def show(self):
        return 'Show word contests!'

class Word(Document):
    def show(self):
        return 'Show word contests!'

documents = [Pdf('Documents1'), Pdf('Documents2'), Word('Documents3')]

for document in documents:
    print document.name + ': ' + document.show()
print


# EXAMPLE 3: Polymorphism with abstract class (most commonly used):
# ==============================================================================
class Car:
    def __init__(self, name):
        self.name = name

    def drive(self):
        raise NotImplementedError('Subclass must implement abstract method')

    def stop(self):
        raise NotImplementedError('Subclass must implement abstract method')

class Sportscar(Car):
    def drive(self):
        return 'Sportscar driving!'

    def stop(self):
        return 'Sportscar breaking!'

class Truck(Car):
    def drive(self):
        return 'Truck driving slowly because heavily loaded.'

    def stop(self):
        return 'Truck breaking!'

cars = [Truck('Bananatruck'), Truck('Orangetruck'), Sportscar('Z3')]

for car in cars:
    print car.name + ': ' + car.drive()