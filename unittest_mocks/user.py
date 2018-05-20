from requests import request
import json

class User:
    def __init__(self):
        self.resp = {}

    def request_users(self, url='https://reqres.in/api/users'):
        self.resp = request('GET', url)

    def request_user(self, user_id=1):
        url = 'https://reqres.in/api/users/{}'.format(user_id)
        return request('GET', url)

    def get_users(self):
        data = json.loads(self.resp.content)
        return data.get('data', [])

    def get_user(self, user_id):
        users = self.get_users()
        for user in users:
            if user.get('id') == user_id:
                return user
        return {}

    def count_users(self, users):
        return len(users)

    def get_description(self):
        return 'My Description'

if __name__ == '__main__':
    user = User()
    user.request_users()
    print
    print 'data:', user.get_users()
    print
    print 'user:', user.get_user(1)
    print
    print 'count:', user.count_users(user.get_users())

