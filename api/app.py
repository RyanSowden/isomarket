import flask 
from flask import request, jsonify, redirect, url_for, session, abort
from home import workers
from auth.register import register
from auth.login import login
from functools import wraps
from add import addMoney
from flask_cors import CORS

app = flask.Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
CORS(app)

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return abort(401, description="You need to login")
    return wrap

@app.route('/test', methods=['GET'])
def books():
    return jsonify(test.books)

@app.route('/auth/register', methods=['POST'])
def registerUser():
    result_register = register().newUser()
    return jsonify(result_register)

@app.route('/auth/login', methods=[ 'POST'])
def loginUser():
    result_login = login().userLogin()
    return listWorker()

@app.route('/add', methods=['GET','POST'])
def get_worker():
    result_add = addMoney().getWorker()
    return jsonify(result_add)

@app.route('/home', methods=['GET'])
def listWorker():
    if not session.get('logged_in'):
        return abort(401, description="You need to login please")
    else:
        result_worker = workers().displayWorker()
        return jsonify(result_worker)
if __name__ == '__main__':
    app.run(debug=True)
