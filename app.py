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
        author = pd.read_csv("C:\\Users\\user\\author.csv", sep=',')        
        for i in author.index:
            author_id = author.iloc[i,0]
            if author_id == request.form['id']:
                owner = author_id
            else:
                owner = author_id

    return render_template("login.html",
                            owner = owner)

@app.route('/register', methods =['GET','POST'])
def register():
    owner = "login ID 을 등록해 주세요."
    if request.method == 'POST':
        author = pd.DataFrame()
        author['id'] = [request.form['id']]
        author['password'] = [request.form['pw']]
        author['profile'] = [request.form['pf']]
        
        author.to_csv("C:\\Users\\user\\author.csv",index=False, line_terminator='\n',encoding='utf-8', mode='a', header=False)
        
        # author['text'] = author['text'].apply(lambda x: x.encode('ascii', 'ignore').decode('ascii'))


        owner = author
    return render_template("register.html",
                            owner = owner)



app.run(port='8888')