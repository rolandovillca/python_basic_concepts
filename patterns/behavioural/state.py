class Language(object):
    def greet(self):
        return self.greeting

class English(Language):
    def __init__(self):
        self.greeting = 'Hello'

class French(Language):
    def __init__(self):
        self.greeting = 'Bonjour'

class Spanish(Language):
    def __init__(self):
        self.greeting = 'Hola'

class multilinguist(object):
    def __init__(self, language):
        self.greetings = {
            'English': 'Hello',
            'French': 'Bonjour',
            'Spanish': 'Hola'
        }
        self.language = language

    def gree(self):
        print self.greetings[self.language]

if __name__ == '__main__':

    # Talking in English:
    translator = multilinguist('English')
    translator.greet()

    # Meets a Frenchman:
    translator.language = 'French'
    translator.greet()

    # Greets a Spaniard:
    translator.language = 'Spanish'
    translator.greet()