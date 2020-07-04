from flask import Flask, render_template, request, jsonify, make_response
import random
import time
import requests
from TikTokApi import TikTokApi
import random
api = TikTokApi()

app = Flask(__name__)


username = "amberbamber88"

toks = api.userLikedbyUsername(username, count=10)

workout_tags = ["keepingactive", "fitness", "indoorworkout", "abs", "challenge", "athomeworkout", "glutes",
                "hips", "legday", "workout", "thicc", "fitnessmotivation", "gains", "strong", "weightlossjourney"]

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
db = []
for t in saved_tiktoks:
    #print(tiktok)
    id = t['id']
    author = t['author']['uniqueId']
    link = "https://www.tiktok.com/" + author + "/video/" + id 
    resp = requests.get('https://www.tiktok.com/oembed?url=' + link)
    if resp.json() == {'status_msg': 'Something went wrong'}:
        print("error")
    else:
        db.append(resp.json()['html'])

random.shuffle(db)


@app.route("/login")
def login():
    """ Route to render the HTML """
    return render_template("login.html")

@app.route("/")
def index():
    """ Route to render the HTML """
    return render_template("main.html", t = db[0])

@app.route("/level2")
def level2():
    """ Route to render the HTML """
    return render_template("level2.html", t = db[0])