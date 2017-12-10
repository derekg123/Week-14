import requests
import facebook
import json
import sqlite3

token = "EAAIvnpZBTjA0BAAweMSaC1JuvB1tHGOHJ55iwkWzLbru28dQwuKpr2AuQYQG82JcNIiuZCozPEZBYus8A9ZA1UZBPQgZCCaU5ScpZCwA3ilbDnxHX7cUSPT7E4HZBCIDODZBKVcY0GUmQuUI2AQjO81EXP3CQlAd0owARSXGZBooF4DAZDZD"
req = "me?fields=posts.limit(100)"

#results = fb_requests(request).json()
#print(results)

CACHE_FNAME = "Facebook_cache.json"

try:
    cache_file = open(CACHE_FNAME,'r')
    cache_contents = cache_file.read()
    cache_file.close()
    CACHE_DICTION = json.loads(cache_contents)
except:
    CACHE_DICTION = {}

#def fb_requests(req):
#    r = requests.get("https://graph.facebook.com/v2.11/" + req , {'access_token' : token}).json()
#    return r

#print(fb_requests(req))

#access_token = "EAAIvnpZBTjA0BAAweMSaC1JuvB1tHGOHJ55iwkWzLbru28dQwuKpr2AuQYQG82JcNIiuZCozPEZBYus8A9ZA1UZBPQgZCCaU5ScpZCwA3ilbDnxHX7cUSPT7E4HZBCIDODZBKVcY0GUmQuUI2AQjO81EXP3CQlAd0owARSXGZBooF4DAZDZD"
#if access_token is None:
#    access_token = input("\nCopy and paste token from https://developers.facebook.com/tools/explorer\n>  ")


#graph = facebook.GraphAPI(access_token)
#posts = graph.get_connections('me','posts')

#def get_fb_posts():
#	while True:
#		try:
#			with open('Facebook_cache.json','a') as f:
#				for post in Posts['data']:
#					f.write(json.dumps(post)+"\n")
#				posts = requests.get(Posts['paging']['next']).json()
#		except KeyError:
#			print("ran out of posts")
#			return(posts)
#			break


def get_fb_posts():
    req = "me?fields=posts.limit(190)"
    if 'Posts' in CACHE_DICTION:
        return CACHE_DICTION['Posts']
    else:
        userposts = requests.get("https://graph.facebook.com/v2.11/" + req , {'access_token' : token}).json()
        try:
            CACHE_DICTION['Posts'] = userposts
            dumped_json_cache = json.dumps(CACHE_DICTION)
            fw = open(CACHE_FNAME, "w")
            fw.write(dumped_json_cache)
            fw.close()
            return CACHE_DICTION['Posts']
        except:
            print("Wasn't in cache and wasn't valid search either")
            return None

plswork = get_fb_posts()

for date in plswork["posts"]["data"]:
    calendar = date["created_time"]
    calonly = 
