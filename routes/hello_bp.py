from flask import Blueprint
from controllers.HelloController import index
hello_bp = Blueprint('hello_bp', __name__)
hello_bp.route('/', methods=['GET'])(index)