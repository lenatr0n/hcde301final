import urllib, urllib2,json

##https://www.googleapis.com/youtube/v3/channels?part=snippet%2CcontentDetails%2Cstatistics&key=[YOUR_API_KEY]' \
##--header 'Authorization: Bearer [YOUR_ACCESS_TOKEN]' \


# example
# https://developers.google.com/apis-explorer/#p/youtube/v3/youtube.search.list?
#         part=snippet
#         &chart=mostPopular
#         &regionCode=es
#         &videoCategoryId=17

def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)
# my api key :
APIKEY = "AIzaSyDYZSV5lF3bBGef0C6ndOvXPzZI7jvb1W8"
baseurl = "https://www.googleapis.com/youtube/v3/videos?"

params= {'key':APIKEY,
        'method':'youtube.search.list',
        'part':'snippet',
        'chart':'mostPopular',
        'regionCode':'us'
        }


url = baseurl + urllib.urlencode(params)
result = urllib2.urlopen(url)
resultlist = result.read()
resultdata = json.loads(resultlist)

#print pretty(resultdata)

def getInfo(resultdata):
        for key in resultdata[['items'][key]['snippet']['title']:
                s +=(key,resultdata[key])
        return s


for x in resultdata:
        print(getInfo(x))
         #print resultdata['items'][x]['snippet']['title']