from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello World!</h1>"

@app.route('/user/<name>')
def user(name):
    user_agent = request.headers.get('User-Agent')
    s = '<h1>Hello,you are {}!</h1>'.format(name)
    s = s+ '<p>Your browser is {}</p>'.format(user_agent)
    return s
