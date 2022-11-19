from flask import Blueprint, jsonify

import logger
import utils

api_bp = Blueprint('api', __name__, url_prefix='/api', template_folder='')
log = logger.get_logger('api')


@api_bp.route("/post/")
def api_posts():
    posts = utils.get_posts_all()
    log.info(f'Запрос /api/posts -> {len(posts)}')
    return jsonify(posts)


@api_bp.route("/post/<int:pk>")
def api_post(pk):
    post = utils.get_post_by_pk(pk)
    log.info(f'Запрос /api/posts/{pk}"')
    return jsonify(post)