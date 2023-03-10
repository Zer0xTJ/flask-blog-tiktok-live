import json


def get_posts():
    return json.load(open('posts.json', 'r'))


def add_post(post):
    posts = get_posts()
    posts.append(post)
    json.dump(posts, open('posts.json', 'w'))


def delete_post(title):
    posts = get_posts()
    posts = [post for post in posts if post['title'] != title]
    json.dump(posts, open('posts.json', 'w'))


# print(get_posts())
# add_post({'title': 'test', 'content': 'test content'})
# print(get_posts())
