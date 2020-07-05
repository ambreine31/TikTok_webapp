from TikTokApi import TikTokApi
api = TikTokApi()
import requests

results = 10

"""
trending = api.trending(count=results)

for tiktok in trending:
    # Prints the text of the tiktok
    print(tiktok['desc'])
    print(tiktok['video'])
"""
"""
username = "amberbamber88"
#username = "tiktok"
try:
    user = api.getUserObject(username)
except:
    print("here!")
"""
#toks = api.userLikedbyUsername(username, count=3000)

#print(user)
#user = api.getUserObject(username)
#user = api.getUser(username)
#print(user)

#6773950055545848837

#hash = api.getSuggestedHashtagsbyID(count=30, userId='6773950055545848837')

#print(hash)

"""
workout_tags = ["keepingactive", "fitness", "indoorworkout", "abs", "challenge", "athomeworkout", "glutes",
                "hips", "legday", "workout", "thicc", "fitnessmotivation", "gains", "strong", "weightlossjourney"]

count = 0
for tiktok in toks:
    count = count +1
    print(count)
    #print(tiktok['textExtra'])
    #print(tiktok)
    if("#" in tiktok['desc']):
        for i in tiktok['textExtra']:
            if(i['hashtagName'] in workout_tags):
                print(i['hashtagName'])
#print(len(trending))
print("final", count)
"""




"""
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
for i in range(len(saved_tiktoks)):
    print(saved_tiktoks[i]['id'])
#db = list()

print(len(saved_tiktoks))
db = []
count = 0
for t in saved_tiktoks:
    #print(tiktok)
    count = count + 1
    print(count)
    id = t['id']
    author = t['author']['uniqueId']
    link = "https://www.tiktok.com/" + author + "/video/" + id 
    resp = requests.get('https://www.tiktok.com/oembed?url=' + link)
    #print(link)
    #print(resp)
    #print(resp.json())
    if resp.json() == {'status_msg': 'Something went wrong'}:
        print("error")
    else:
        db.append(resp.json()['html'])

print(len(db))
"""



toks = api.byHashtag('workout', count=1)

#print(toks)
for tiktok in toks:
    #print(tiktok)
    #print(tiktok['itemInfos']['text'])
    #print(tiktok['textExtra'])
    #print(tiktok)
    t = api.getTikTokById(tiktok['itemInfos']['id'])
    print(t)
    print(t[itemInfo][itemStruct][author])
    #print(t['author']['uniqueId'])
"""
count = 30

tiktoks = api.byHashtag('funny', count=count)

for tiktok in tiktoks:
    print(tiktok['itemInfos']['text'])
"""
