from flask import Flask, render_template, redirect, request
import pandas as pd


app = Flask(__name__,
            template_folder='template' )
app.config['ENV'] ='Development'
app.config['DEBUG'] = True

app.secret_key = 'who are you?'


@app.route('/')
def index():
    owner = 'Hi~ Everyone~'
    return render_template('template.html',
                            owner = owner)

@app.route('/login', methods=['GET', 'POST'])
def login():
    owner = 'Hi~ Everyone~'
    if request.method == 'POST':
        owner = 'welcome login'
    return render_template("login.html",
                            owner = owner)

@app.route('/register', methods =['GET','POST'])
def register():
    owner = "login ID 을 등록해 주세요."
    if request.method == 'POST':
        owner = request.form['id']

    return render_template("register.html",
                            owner = owner)



app.run(port='8888')