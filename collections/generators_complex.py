import requests

# Using example of https://jsonplaceholder.typicode.com/

REQUEST_POSTS = 'https://jsonplaceholder.typicode.com/posts'
REQUEST_COMMENTS = 'https://jsonplaceholder.typicode.com/comments'
REQUEST_ALBUMS = 'https://jsonplaceholder.typicode.com/albums'
REQUEST_PHOTOS = 'https://jsonplaceholder.typicode.com/photos'
REQUEST_TODOS = 'https://jsonplaceholder.typicode.com/todos'
REQUEST_USERS = 'https://jsonplaceholder.typicode.com/users'

users = requests.get(REQUEST_USERS)

# print users.json()

def user_generator():
    for user in users:
        yield user
