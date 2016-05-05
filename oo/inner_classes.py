'''
An inner class or nested class is a defined entirely within the body of another class
'''


# EXAMPLE 1:
# ==============================================================================
# An inner class or nested class is a defined entirely
# within the body of another class

class Human:
    def __init__(self):
        self.name = 'Guido'
        self.head = self.Head()

    class Head:
        def talk(self):
            return 'Talking...'

if __name__ == '__main__':
    guido = Human()
    print guido.name
    print guido.head.talk()
    print


# EXAMPLE 2:
# ==============================================================================
# By using inner classes you can make your code even more object orientated.
# A single object can hold several sub objects.
# We can use them to add more structure to our programs.
class Human2:

    def __init__(self):
        self.name = 'Guido'
        self.head = self.Head()
        self.brain = self.Brain()

    class Head:
        def talk(self):
            return 'talking...'

    class Brain:
        def think(self):
            return 'thinking...'

if __name__ == '__main__':
    guido = Human2()
    print guido.name
    print guido.head.talk()
    print guido.brain.think()