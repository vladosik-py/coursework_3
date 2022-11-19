from flask import Flask, request, render_template

import utils
from api.api import api_bp

app = Flask(__name__)


@app.route("/", methods=['GET'])
def all_posts():
    posts = utils.get_posts_all()
    return render_template('index.html', posts=posts)


@app.route("/posts/<int:pk>", methods=['GET'])
def get_post(pk):
    post = utils.get_post_by_pk(pk)
    comments = utils.get_comments_by_post_id(pk)
    return render_template('post.html', post=post, comments=comments)


@app.route("/search/")
def search_page():
    word = request.args.get('s', '').lower()
    posts = utils.search_for_posts(search_word=word)
    return render_template('index.html', posts=posts)


@app.route("/user/<user_name>")
def get_user(user_name):
    posts = utils.get_posts_by_user(user_name=user_name)
    return render_template('index.html', posts=posts)


@app.errorhandler(404)
def not_found(oops):
    return "404 Not Found"


@app.errorhandler(500)
def server_error(oops):
    return "500 Internal Server Error"


app.register_blueprint(api_bp)

if __name__ == '__main__':
    app.run(debug=True)