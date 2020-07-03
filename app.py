from flask import Flask, render_template, request, jsonify, make_response
import random
import time
import requests
from TikTokApi import TikTokApi
api = TikTokApi()

app = Flask(__name__)


username = "amberbamber88"

toks = api.userLikedbyUsername(username, count=1000)

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
db = list()
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




posts = len(saved_tiktoks) # num posts to generate

quantity = 3 # num posts to return per request

@app.route("/login")
def login():
    """ Route to render the HTML """
    return render_template("login.html")

@app.route("/")
def index():
    """ Route to render the HTML """
    return render_template("index.html")


@app.route("/load")
def load():
    """ Route to return the posts """

    time.sleep(0.2)  # Used to simulate delay

    if request.args:
        counter = int(request.args.get("c"))  # The 'counter' value sent in the QS

        if counter == 0:
            print(f"Returning posts 0 to {quantity}")
            # Slice 0 -> quantity from the db
            res = make_response(jsonify(db[0: quantity]), 200)

        elif counter == posts:
            print("No more posts")
            res = make_response(jsonify({}), 200)

        else:
            print(f"Returning posts {counter} to {counter + quantity}")
            # Slice counter -> quantity from the db
            res = make_response(jsonify(db[counter: counter + quantity]), 200)

    return res

"""
from flask import Flask, render_template, Response
import requests
from TikTokApi import TikTokApi
api = TikTokApi()
app = Flask(__name__)


username = "amberbamber88"

toks = api.userLikedbyUsername(username, count=100)

workout_tags = ["keepingactive", "fitness", "indoorworkout", "abs", "challenge", "athomeworkout", "glutes",
                "hips", "legday", "workout", "thicc", "fitnessmotivation", "gains", "strong", "weightlossjourney"]

saved_tiktoks = []

for tiktok in toks:
    fitness = False
    if("#" in tiktok['desc']):
        for i in tiktok['textExtra']:
            if(i['hashtagName'] in workout_tags):
                print(i['hashtagName'])
                fitness = True
    if(fitness == True):
        saved_tiktoks.append(tiktok)
    

embed_array = []
for t in saved_tiktoks:
    #print(tiktok)
    id = t['id']
    author = t['author']['uniqueId']
    link = "https://www.tiktok.com/" + author + "/video/" + id 
    resp = requests.get('https://www.tiktok.com/oembed?url=' + link)
    embed_array.append(resp.json()['html'])

@app.route('/')
def hello_world():
    return render_template('index.html', tiktoks = embed_array)
"""