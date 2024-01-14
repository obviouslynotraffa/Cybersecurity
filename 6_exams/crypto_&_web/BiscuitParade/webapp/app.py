from flask import Flask, render_template, make_response, request

app = Flask(__name__)


@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method=='GET':
        resp = make_response(render_template('index.html'))
        resp.set_cookie('permission', 'user')
        return resp
    elif request.method=='POST':
        cookie = request.cookies.get('permission')
        if cookie == 'admin':
            resp = make_response(render_template('flag.html'))
        else:
            print(f'[!] Cookie = {cookie}')
            resp = make_response(render_template('nope.html'))
        return resp

@app.route('/flag/')
def flag():
    return render_template('flag.html')

@app.route('/nope/')
def nope():
    return render_template('nope.html')

# @app.route('/login')
# def hello():
#     return '<h1>Hello, World!</h1>'
