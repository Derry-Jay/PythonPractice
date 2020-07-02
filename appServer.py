from flask import Flask, render_template as rt, redirect, url_for, session, request as rq
import os
from FunctionalModules import *
# import dbops as pdb
app = Flask(__name__)
l = []
app.secret_key = "Gene_Ontology"
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)


def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path, endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)


def blend(f1, f2):
    return lambda a, **b: f1(f2(a, **b))


goto = blend(redirect, url_for)


@app.route('/welcome')
def welcome():
    return rt('index.html')


@app.route('/signup')
def signup():
    return rt('signup.vue')
# @a
# @a
# @app.route('/disease', methods=['POST', 'GET'])
# def dispdis():
# @app.route('//')
# def
# @a
# @a
@app.route('/success/<uname>/<utp>/<sex>/<city>', methods=['POST', 'GET'])
def success(uname, utp, sex, city):
    if session != {}:
        return rt('home.vue', name=uname, utype=utp, gender=sex, city=city)
    else:
        return goto('login')


@app.route('/logout')
def logout():
    if session != {}:
        session.pop('user_name')
        session.pop('user_type')
    return goto('login')


@app.route('/login', methods=['POST', 'GET'])
def login():
    a = dict(rq.form)
    for c in a:
        l.append(a[c])
    pf = pdb.ins(l)
    if pf:
        return rt('login.vue')
    else:
        return goto('signup')


@app.route('/', methods=['POST', 'GET'])
def check():
    prd = dict(rq.form)
    prl = []
    c = 0
    for i in prd:
        prl.append(prd[i])
    c = pdb.get(prl)
    if c == 1 and session == {} and '' not in prl and prl != []:
        a = pdb.get1(prl)
        session['user_name'] = a[0]
        session['user_type'] = a[1]
        return goto('success', uname=a[0], utp=a[1], sex=a[2], city=a[3])
    else:
        return goto('login')


if __name__ == "__main__":
    app.run(debug=True)
