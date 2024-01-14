from flask import Flask, render_template, make_response, request

app = Flask(__name__)


@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method=='GET':
        resp = make_response(render_template('index.html'))
        resp.set_cookie('permission', '04f8996da763b7a969b1028ee3007569eaf3a635486ddab211d512c85b9df8fb') # use the sha-256 user hash
        return resp
    elif request.method=='POST':
        cookie = request.cookies.get('permission')
        if cookie == '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918':
            resp = make_response(render_template('flag.html'))
        else:
            print(f'[!] Cookie = {cookie}')
            resp = make_response(render_template('error.html'))
        return resp

@app.route('/flag/')
def flag():
    return render_template('flag.html')

@app.route('/error/')
def nope():
    return render_template('error.html')
