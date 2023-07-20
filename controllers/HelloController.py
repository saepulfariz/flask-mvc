# pseudo code
import sys
from flask import render_template, redirect, url_for, request, abort
# from models.User import User
# from flask_sqlalchemy import SQLAlchemy
# db = SQLAlchemy()
def index():
    print('Hello Controller')
    data = {
        'title' :'Hello Controller',
        'data' :'Data Controller',
    }
    return render_template('hello.html', data = data)