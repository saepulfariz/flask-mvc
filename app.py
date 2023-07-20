from flask import Flask, render_template, session, flash
from flask_migrate import Migrate
from models.User import db
from libraries.Alert import Alert
from routes.user_bp import user_bp
from routes.hello_bp import hello_bp

from CustomRequest import CustomRequest, MethodSpooferMiddleware
# https://blog.carsonevans.ca/2020/07/06/request-method-spoofing-in-flask/

from flask_wtf.csrf import CSRFProtect
# pip install flask-wtf
# https://flask-wtf.readthedocs.io/en/0.15.x/csrf/#csrf

app = Flask(__name__)

csrf = CSRFProtect(app)

app.request_class = CustomRequest
app.wsgi_app = MethodSpooferMiddleware(app.wsgi_app)
app.config.from_object('config')
db.init_app(app)
migrate = Migrate(app, db)
app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(hello_bp, url_prefix='/hello')

from flask_wtf.csrf import CSRFError

@app.errorhandler(CSRFError)
def handle_csrf_error(e):
    data = {
        'title' : 'Token is required'
    }
    return render_template('template/error/csrf.html', reason=e.description, data=data), 400

@app.context_processor
def def_inject_custom_filters():
    return dict(custom_filter=Alert.get())

@app.route('/')
def index():
    data = {
        'title' : 'Home Page'
    }
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.debug = True
    app.run()