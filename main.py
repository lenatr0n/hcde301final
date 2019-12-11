import webapp2
import os, jinja2
import json

##https://www.googleapis.com/youtube/v3/channels?part=snippet%2CcontentDetails%2Cstatistics&key=[YOUR_API_KEY]' \
##--header 'Authorization: Bearer [YOUR_ACCESS_TOKEN]' \

# my api key : AIzaSyDYZSV5lF3bBGef0C6ndOvXPzZI7jvb1W8
#https://www.googleapis.com/youtube/v3/videos?

baseurl = 'hhttps://www.googleapis.com/youtube/v3/search'

JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# class MainHandler(webapp2.RequestHandler):
#     def get(self, baseurl = 'https://www.googleapis.com/youtube/v3/search'):
#
#         template = JINJA_ENVIRONMENT.get_template('index.html')
#


def main():
