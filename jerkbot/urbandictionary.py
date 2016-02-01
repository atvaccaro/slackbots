import urllib2
import json

base_url = 'http://api.urbandictionary.com/v0/define?term='

def urban_define(term):
    opener = urllib2.build_opener()
    the_page = opener.open(base_url + term.replace(' ', '+'))
    
    json_page = json.load(the_page)
    
    return json_page['list'][0]['definition']

if __name__ == '__main__':
    print(urban_define('foo'))
