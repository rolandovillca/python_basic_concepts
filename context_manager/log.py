class Log:
    def __init__(self, filename):
        print '__init__'
        self.filename = filename
        self.fp = None

    def logging(self, text):
        print 'into logging method {}'.format(text)
        self.fp.write(text + '\n')

    def __enter__(self):
        print '__enter__'
        self.fp = open(self.filename, 'a+')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print '__exit__'
        self.fp.close()

with Log('file.log') as logfile:
    print 'Main'
    logfile.logging('Test1')
    logfile.logging('Test2')
