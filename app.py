from flask import Flask, render_template, request, jsonify, make_response,g, redirect, session, Response, url_for, flash
import random
import requests
from TikTokApi import TikTokApi
import pickle
api = TikTokApi()


class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'

#users = []
#users.append(User(id=1, username='user', password='mdp'))
user = [User(id=1, username='user', password='mdp')]

app = Flask(__name__)
app.secret_key = 'courgette'

@app.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        #user = [x for x in users if x.id == session['user_id']][0]
        g.user = user
        
#username = "amberbamber88"
db = pickle.load( open( "db.p", "rb" ) )

def Get_TikToks(toks):

    workout_tags = ["keepingactive", "fitness", "indoorworkout", "abs", "challenge", "athomeworkout", "glutes",
                "legday", "workout", "fitnessmotivation", "gains", "strong", "weightlossjourney"]

    saved_tiktoks = []

    for tiktok in toks:
        fitness = False
        if("#" in tiktok['desc']):
            for i in tiktok['textExtra']:
                if(i['hashtagName'] in workout_tags):
                    #print(i['hashtagName'])
                    fitness = True
        if(fitness == True):
            saved_tiktoks.append(tiktok)

    #db = list()
    db_f = []
    for t in saved_tiktoks:
        #print(tiktok)
        id = t['id']
        author = t['author']['uniqueId']
        link = "https://www.tiktok.com/" + author + "/video/" + id 
        resp = requests.get('https://www.tiktok.com/oembed?url=' + link)
        if resp.json() == {'status_msg': 'Something went wrong'}:
            print("error")
        else:
            db_f.append(resp.json()['html'])

    random.shuffle(db_f)
    print(len(db_f))
    print("here")
    pickle.dump( db_f, open( "db.p", "wb" ) )

@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)

        option = request.form['submit_button']

        if(option == "user"):
            username = request.form['username']
            print(username)
            try:
                toks = api.userLikedbyUsername(username, count=200)
                Get_TikToks(toks)
                session['user_id'] = 1
                return redirect(url_for('level1'))
            except:
                print('user error')
                return redirect('/')
    return render_template('login.html')

@app.route("/level1")
def level1():
    if not g.user:
        return redirect('/login')
    #db = request.args['db']
    db = pickle.load( open( "db.p", "rb" ) )
    print(len(db))
    #messages = session['db']
    return render_template("level1.html", t1 = db[0], t2 = db[1])

@app.route("/level2")
def level2():
    if not g.user:
        return redirect('/login')
    db = pickle.load( open( "db.p", "rb" ) )
    return render_template("level2.html", t1 = db[2], t2 = db[3])

@app.route("/level3")
def level3():
    if not g.user:
        return redirect('/login')
    db = pickle.load( open( "db.p", "rb" ) )
    return render_template("level3.html", t1 = db[4], t2 = db[5])

@app.route("/transition1")
def transition1():
    if not g.user:
        return redirect('/login')
    return render_template("transition1.html")

@app.route("/transition2")
def transition2():
    if not g.user:
        return redirect('/login')
    return render_template("transition2.html")

@app.route("/final")
def final():
    if not g.user:
        return redirect('/login')
    return render_template("final.html")