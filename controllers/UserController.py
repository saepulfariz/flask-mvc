# pseudo code
import sys
from flask import render_template, redirect, url_for, request, abort, session
from models.User import db, User
# from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from libraries.Alert import Alert
# db = SQLAlchemy()
title = 'User CRUD'
def index(): 

    sql  = text('SELECT * FROM users WHERE age = :age')
    result = db.session.execute(sql, {'age': '23'})
    # 
    # result = User.query.order_by(text('id desc')).all()
    result = User.query.order_by(User.id.desc()).all()
    # result = User.query.order_by(User.id.asc()).all()

    # where
    # user = User.query.filter_by(id=userId).first()

    print(result)
    # names = [row[1] for row in result]
    # print(names)
    data  = {
        'title' : title,
        # 'users' : User.query.all(),
        'users' : result,
    }
    return render_template('users/index.html', data = data)
def show(userId):
    user = User.query.get_or_404(userId)
    # user = User.query.get(userId)
    data  = {
        'title' : title,
        'user' : user,
    }
    return render_template('users/show.html', data = data)
def new(): 
    data  = {
        'title' : title,
    }
    return render_template('users/new.html', data = data)
def create():
    name = request.form['name']
    age = request.form['age']
    address = request.form['address']
    user = User(name=name, age=age, address=address)
    db.session.add(user)
    db.session.commit()
    Alert.set('success', 'success', 'Add success')
    
    return redirect(url_for('user_bp.index'))

def edit(userId):
    user = User.query.get_or_404(userId)
    # user = User.query.filter_by(id=userId).first()
    # user = User.query.get(userId)
    data  = {
        'title' : title,
        'user' : user,
    }
    return render_template('users/edit.html', data = data)
def update(userId):
    user = User.query.get_or_404(userId)
    user.name = request.form['name']
    user.age = request.form['age']
    user.address = request.form['address']
    db.session.commit()
    Alert.set('success', 'success', 'Update success')
    return redirect(url_for('user_bp.index'))
def delete(userId):
    user = User.query.get_or_404(userId)
    db.session.delete(user)
    db.session.commit()
    Alert.set('success', 'success', 'delete success')
    return redirect(url_for('user_bp.index'))
def destroy(userId):
    ...