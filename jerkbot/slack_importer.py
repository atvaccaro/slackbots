import os
import json
from db import cursor, conn
import config, permissions

base_directory = 'lol-xd'#raw_input('Dir name: ')
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
                        cursor.execute('INSERT INTO user VALUES(?, ?, ?, ?)', (user['id'], user['name'], permissions.USER, config.starting_beers))
                        conn.commit()
                    except Exception, e:
                        print str(e)
            else:
                for message in data:
                    try:
                        cursor.execute('INSERT INTO message VALUES(?, ?)', (message['user'], message['text']))
                    except Exception, e:
                        print str(e)
                conn.commit()
