from flask import Flask
from flask.helpers import make_response
from flask.wrappers import Request
from flask import request
from werkzeug.wrappers import response
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Here we go again.</h1>'


#dynamic route

@app.route('/user/<name>')
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


@app.route('/bad_request')
def bad_request():
    return '<h1>Bad Request</h1>', 400


@app.route('/cookie')
def cookie():
    response = make_response('<h1>This document carries a cookie!</h>')
    response.set_cookie('answer', '42')
    return response

    