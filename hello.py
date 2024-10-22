from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)











# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def index():
#     return '<h1>Hello World!</h1>'

# @app.route('/user/<sapna>')
# def user(sapna):
#     return '<h1>Hello, {}!</h1>'.format(sapna)
