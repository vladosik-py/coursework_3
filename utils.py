import json


def load_posts_from_json(file_name):
    """загружает данные из файла"""
    with open(file_name, encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_posts_all():
    """возвращает посты"""
    posts = load_posts_from_json('data/posts.json')
    return posts


def get_posts_by_user(user_name=None):
    """возвращает посты определенного пользователя"""
    posts = load_posts_from_json('data/posts.json')

    if user_name:
        posts = filter(lambda x: user_name == x['poster_name'].lower(), posts)

    return posts


def get_comments_by_post_id(post_id):
    """возвращает комментарии определенного поста"""
    all_comments = load_posts_from_json('data/comments.json')
    comments = []
    for comment in all_comments:
        if comment['post_id'] == post_id:
            comments.append(comment)
    return comments


def search_for_posts(search_word=None):
    """возвращает список постов по ключевому слову"""
    posts = load_posts_from_json('data/posts.json')

    if search_word:
        posts = filter(lambda x: search_word in x['content'].lower(), posts)

    return posts


def get_post_by_pk(pk):
    """возвращает один пост по его идентификатору"""
    posts = load_posts_from_json('data/posts.json')
    for post in posts:
        if post['pk'] == pk:
            return post