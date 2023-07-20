#FLASK

masuk ke env flask dulu

- python -m venv venv
- venv\Scripts\activate.bat
- pip install flask
- pip install -r requirements.txt
- pip freeze > requirements.txt

- pip install python-dotenv
  pip install Flask-Migrate
  pip install flask-wtf
  pip install mysqlclient
  flask db init // bikin folder migrate
  flask db migrate // bikin file migrate dari model
  flask db upgrade
  flask db downgrade
  kosong kan folder migration

  pip install Flask-session
  pip uninstall Flask-session

  pip install pytz

export FLASK_APP="mainfilename.py"
export FLASK_DEBUG=1
python -m flask run --host=0.0.0.0

HTTP SPOOFING
https://blog.carsonevans.ca/2020/07/06/request-method-spoofing-in-flask/

CSRF
https://flask-wtf.readthedocs.io/en/0.15.x/csrf/#csrf

https://hackersandslackers.com/plotly-dash-with-flask/
https://www.loginworks.com/blogs/making-web-application-crud-using-flask-and-mysql/
https://www.tutorialspoint.com/flask/flask_templates.htm
https://python.plainenglish.io/flask-crud-application-using-mvc-architecture-3b073271274f
https://python.plainenglish.io/flask-restful-apis-72e05f8d41fa
