import urllib2
import json

urban_base_url = 'http://api.urbandictionary.com/v0/define?term='

def urban_define(term):
    opener = urllib2.build_opener()
    the_page = opener.open(urban_base_url + term.replace(' ', '+'))

    json_page = json.load(the_page)

    return json_page['list'][0]['definition']

def define(term):
    pass

def get_synonyms(term):
    pass
