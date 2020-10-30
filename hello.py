from flask import Flask, request,render_template

app = Flask(__name__)

@app.route('/')
def index():
    # return "<h1>Hello World!</h1>"
    return render_tenmplate('index.html')

@app.route('/user/<name>')
def user(name):
    # 直接实现的代码
    '''
    user_agent = request.headers.get('User-Agent')
    s = '<h1>Hello,you are {}!</h1>'.format(name)
    s = s+ '<p>Your browser is {}</p>'.format(user_agent)
    return s
    ''' 
    # 利用模板的代码
    return render_template('user.html',name=name)

