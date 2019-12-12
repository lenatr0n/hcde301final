import webapp2
import os, jinja2
import logging
import urllib, urllib2,json

baseurl = 'hhttps://www.googleapis.com/youtube/v3/search'

JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


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
        embedURL1 ='<iframe id="ytplayer" type="text/html" width="720" height="405" src="https://www.youtube.com/embed/'
        embedURL2 = '"frameborder="0" allowfullscreen>'
        data = []
        for video in resultdata['items']:
                data.append({
                    'title': video['snippet']['title'],
                    'url': youtubeBaseUrl + video['id'],
                    'videoID': video['id']
                })

        return data


class MainHandler(webapp2.RequestHandler):
    def get(self):
        payload = {'text': 'hello World'}
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(payload))

    def post(self):
        country = self.request.get('country')
        category = self.request.get('category')
        topVideos = getTopVideos(country, category)
        data = {'topVideos': topVideos}
        template = JINJA_ENVIRONMENT.get_template('topViews.html')
        self.response.write(template.render((data)))




application = webapp2.WSGIApplication([('/', MainHandler)], debug=True)
