#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import jinja2
import webapp2
import os
import urllib2
import json
from google.appengine.api import users
from google.appengine.ext import ndb
import logging
import datetime

#associated with surveyhandler
class User(ndb.Model):
        username = ndb.StringProperty(required=True)
        useful= ndb.StringProperty(required=True)
        created_date = ndb.DateTimeProperty(required=True)

# word page datastore attempt
class WordPageUser(ndb.Model):
        word = ndb.StringProperty(required=True)
        created_date = ndb.DateTimeProperty(required=True)

#allow user to go to do log out in a more convenient way
class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user() #getting current user
        useracc = users.create_logout_url('/') #variable for user to sign out
        template_vars={'signout_url' : useracc} #library to store all the variable
        entry = jinja2_environment.get_template('template/welcome.html')
        self.response.write(entry.render(template_vars))
        self.response.write('<html><body>%s</body></html>')

#allow user to log in then redirect them straight to home page (aka welcome page)
class HomePageHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        login_url = users.create_login_url('/')
        useracc = users.create_logout_url('/') #variable for user to sign out

        entry_vars = {'login_url': login_url, 'user': user, 'signout_url': useracc}

        logging.info("User is %s" %user)
        entry = jinja2_environment.get_template('template/welcomePage.html')
        self.response.write(entry.render(entry_vars))

# #allow user to take survey when they choose your thoughts
class SurveyHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        username = self.request.get('username')
        login_url = users.create_login_url('/')
        useracc = users.create_logout_url('/')
        template_vars={'username' : username,
                    'login_url': login_url,
                     'user': user, 'signout_url': useracc}
        entry = jinja2_environment.get_template('template/third.html')
        self.response.write(entry.render(template_vars))


    def post(self):
        #the name that user input in the font
        username = self.request.get('username')
        #the respond they gave to the website, how they think about the web application
        useful = self.request.get('useful')

        current_date = datetime.datetime.now()
        username1 = User (username=username, useful=useful)
        username1.created_date = current_date
        username1.put()


        user = users.get_current_user()
        login_url = users.create_login_url('/')
        useracc = users.create_logout_url('/')
        template_vars={'username' : username,
                    'login_url': login_url,
                     'user': user, 'signout_url': useracc}
        entry = jinja2_environment.get_template('template/third.html')
        self.response.write(entry.render(template_vars))

# #store user data from the survey
# class UserDataHandler(webapp2.RequestHandler):
#     def get(self):
#         query = Survey.query()
#         user_data = query.fetch()
#
#
#         template_vars = {'username':user_data, 'login_url': login_url,
#          'user': user, 'signout_url': useracc}
#         template = jinja_environment.get_template(
#             'templates/third.html')
#         self.response.write(template.render(template_vars))
#

#handler for datastore
class WordDataHandler(webapp2.RequestHandler):
    def get(self):
        query = Survey.query()
        word_data = query.fetch()

        template_vars = {'username':user_data, 'login_url': login_url,
         'user': user, 'signout_url': useracc}
        template = jinja_environment.get_template(
            'templates/third.html')
        self.response.write(template.render(template_vars))


#handler for the bubble map
class NodeHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        username = self.request.get('username')
        login_url = users.create_login_url('/')
        useracc = users.create_logout_url('/')
        url = ("http://randomword.setgetgo.com/get.php")
        string = urllib2.urlopen(url).read()
        # json.loads(string)
        # returns a dictionary
        logging.info(">>>>>>>>>>" + string)
        word = string
        #bigdictionary = string


        #word = bigdictionary['word']
        print (word)
        # temp = Temperature(temperature = int(howhot), created = datetime.datetime.now(),
        #     latitude = float(lat), longitude = float(lon))
        # temp.put()

        # def post(self):
        #     username = self.request.get('username')
        #     current_date = datetime.datetime.now()
        #     username1 = WordPageUser (word=word)
        #     username1.created_date = current_date
        #
        #     username1.put()

        template_vars={'username' : username,
                    'login_url': login_url,'word' : word,
                     'user': user, 'signout_url': useracc}
        template = jinja2_environment.get_template('template/wordPage.html')
        self.response.write(template.render(template_vars))


        # set up tempalte_vars dictionary from html {{}}
        # template_vars = {'temperature' : howhot, 'form': form}
        # self.response.write(template.render(template_vars))

# #handler for the About Us page, which is the last page
class AboutHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        username = self.request.get('username')
        login_url = users.create_login_url('/')
        useracc = users.create_logout_url('/')
        template_vars={'username' : username,
                    'login_url': login_url,
                     'user': user, 'signout_url': useracc}

        entry = jinja2_environment.get_template('template/aboutUs.html')
        self.response.write(entry.render(template_vars))

jinja2_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

app = webapp2.WSGIApplication([
    ('/', HomePageHandler),
    ('/logIn', MainHandler),
    ('/word', NodeHandler),
    ('/feedBack', SurveyHandler),
    ('/aboutUs', AboutHandler)
], debug=True)
