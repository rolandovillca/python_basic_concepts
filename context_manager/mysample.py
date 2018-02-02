class myclass:
    def __init__(self):
        print '__init__'

    def __enter__(self):
        print '__enter__'
        return self

    def __exit__(self, type, value, traceback):
        print '__exit__'

    def __del__(self):
        print '__del__'

    def hello(self, text):
        print 'hello', text

with myclass() as mc:
    print 'body'
    print mc.hello('rolando')

print mc.hello('again')
