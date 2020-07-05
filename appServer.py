from flask import Flask, render_template, session, redirect, url_for
app = Flask(__name__)
def blend(f1,f2):
    return lambda a,**b: f1(f2(a,**b))
goto = blend(redirect,url_for)
@app.route('/signup')
def signup(parameter_list):
    return render_template('signup.vue')
@app.route('/welcome')
def welcome():
    return render_template('index.vue')
if __name__=="__main__":
    app.run(debug=True)