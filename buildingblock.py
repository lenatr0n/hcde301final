import urllib, urllib2,json
def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)
# my api key :
APIKEY = "AIzaSyDYZSV5lF3bBGef0C6ndOvXPzZI7jvb1W8"
baseurl = "https://www.googleapis.com/youtube/v3/videos?"

def getTopVideos(regionCode, category):
        params= {'key':APIKEY,
                'method':'youtube.search.list',
                'part':'snippet',
                'chart':'mostPopular',
                'regionCode': regionCode,
                'videoCategoryId': category
                }


        url = baseurl + urllib.urlencode(params)
        result = urllib2.urlopen(url)
        resultlist = result.read()
        resultdata = json.loads(resultlist)

        youtubeBaseUrl = 'https://www.youtube.com/watch?v='

        print pretty(resultdata)

        for thing in resultdata['items']:
                print(thing['snippet']['title'])
                print(youtubeBaseUrl + thing['id'])


getTopVideos('us',1)