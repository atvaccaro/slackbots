import urllib2
import json

urban_base_url = 'http://api.urbandictionary.com/v0/define?term='

def urban_define(text):
    opener = urllib2.build_opener()
    the_page = opener.open(urban_base_url + ''.join(text[1:]).replace(' ', '+'))

    json_page = json.load(the_page)

    try:
        return json_page['list'][0]['definition']
    except Exception:
        return 'No definition found. :disappointed:'

def define(term):
    pass

def get_synonyms(term):
    pass
