import requests

class Blog:
    def __init__(self, name, url='https://jsonplaceholder.typicode.com/posts'):
        self.name = name
        self.url = url

    def posts(self):
        response = requests.get(url)
        return response.json()

    def __repr__(self):
        return '<Blog: {}>'.format(self.name)
