from flask import Blueprint
from controllers.UserController import index, new, create, show, edit, update, destroy, delete
user_bp = Blueprint('user_bp', __name__)
user_bp.route('/', methods=['GET'])(index)
user_bp.route('/new', methods=['GET'])(new)
user_bp.route('/', methods=['POST'])(create)
user_bp.route('/<int:userId>', methods=['GET'])(show)
user_bp.route('/<int:userId>/edit', methods=['GET'])(edit)
user_bp.route('/<int:userId>', methods=['DELETE'])(delete)
user_bp.route('/<int:userId>', methods=['PUT'])(update)

# user_bp.route('/<int:userId>', methods=['POST'])(update)
# user_bp.route('/<int:userId>', methods=['DELETE'])(destroy)
# user_bp.route('/<int:userId>', methods=['DELETE'])(destroy)