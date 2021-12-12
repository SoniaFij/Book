from flask import Flask
from flask.helpers import make_response
from flask.json import load
from flask.wrappers import Request
from flask import request, redirect, abort, render_template
from werkzeug.wrappers import response
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime


app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
def index():
    return render_template('home.html')

#dynamic route

@app.route('/user_old/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)


""" @app.route('/context')
def context():
    user_agent = request.headers.get('User-Agent')
    print("var1 = " + request.args["var1"] + " and var2 = " + request.args["var2"])
    return '<p>Your browser is {}</p>'.format(user_agent) """

#URL: http://127.0.0.1:5000/context?var1=babcia_czeslawa&var2=tata


@app.route('/browser')
def browser():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is {}</p>'.format(user_agent)


@app.route('/connection')
def connection():
    connection_type = request.headers.get('Connection')
    return '<p>Browser connection type: {}</p>'.format(connection_type)


#adding status code example

@app.route('/bad_request')
def bad_request():
    return '<h1>Bad Request</h1>', 400


#response object in a view function example: adding cookie

@app.route('/cookie')
def cookie():
    response = make_response('<h1>This document carries a cookie!</h>')
    response.set_cookie('answer', '42')
    return response


#redirect response example

@app.route('/redirect')
def redirect_example():
    return redirect('https://www.google.pl')


#special response: abort (error handling - returns status code 404 if the id dynamic argument
#given in the URL does not represent a valid user)

""" @app.route('/userid/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>Hello, {}</h1>'.format(user.name) """
 

#adding jinja template

@app.route('/jinja_example')
def jinja_example():
    return render_template('index.html')


@app.route('/user/<name>')
def userjinja(name):
    return render_template('user2.html', name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/sum/<int:first_int>/<int:second_int>')
def sum(first_int, second_int):
    sum = (first_int + second_int)
    return '%d + %d = %d' % (first_int, second_int, sum)

@app.route(('/sum_t/<int:first_int>/<int:second_int>'))
def sum_t(first_int, second_int):
    sum_t = first_int + second_int
    return render_template('sum_t.html', first_int=first_int, second_int=second_int, sum_t = sum_t)






    