from flask import Flask
from flask.wrappers import Request
from flask import request
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

