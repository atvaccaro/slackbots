import os
import json
import re
from db import cursor, conn
import config, permissions

DEBUG = False
base_directory = raw_input('Dir name: ')
# Import users first
for root, subdirs, filenames in os.walk(base_directory):
    for filename in filenames:
        if filename in ('channels.json', 'integration_logs.json'):
            continue
        with open(os.path.join(root, filename)) as f:
            data = json.loads(f.read())
            if filename == 'users.json':
                for user in data:
                    try:
                        print 'Loading ' + user['name']
                        if not DEBUG: cursor.execute('INSERT INTO user VALUES(?, ?, ?, ?)', (user['id'], user['name'], permissions.USER, config.starting_beers))
                        conn.commit()
                    except Exception, e:
                        print str(e)
            else:
                for message in data:
                    try:
                        if not message.get('subtype'): #assume anything without a subtype is a regular message
                            text = message['text']
                            text = re.sub(r'[`]+[^`]+[`]+', '', text) #triple code tags
                            text = re.sub(r'<[^>]+>', '', text) #urls
                            text = re.sub(r"[^a-zA-Z']", ' ', text).encode('ascii','ignore') #non-alphanumerics, asciiz
                            text = start_char + text + end_char
                            print text
                            if not DEBUG: cursor.execute('INSERT INTO message VALUES(?, ?)', (message['user'], text))
                    except Exception, e:
                        print str(e)
                conn.commit()
if DEBUG: print "WARNING: WAS RUN IN DEBUG MODE; NOTHING SAVED TO DB"
