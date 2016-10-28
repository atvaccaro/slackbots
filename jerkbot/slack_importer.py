import os
import json
import re
import enchant
from db import cursor, conn
import config

checker = enchant.Dict('en_US')
DEBUG = False
base_directory = raw_input('Dir name: ')
# Import users first
for root, subdirs, filenames in os.walk(base_directory):
    for filename in filenames:
        if filename in ('channels.json', 'integration_logs.json', '.DS_Store'):
            continue
        with open(os.path.join(root, filename)) as f:
            data = json.loads(f.read())
            if filename == 'users.json':
                for user in data:
                    try:
                        print('Loading ' + user['name'])
                        if not DEBUG: cursor.execute('INSERT INTO user VALUES(?, ?, ?, ?)', (user['id'], user['name'], permissions.USER, config.starting_beers))
                        conn.commit()
                    except Exception as e:
                        print(e)
            else:
                for message in data:
                    try:
                        if not message.get('subtype'): # assume anything without a subtype is a regular message
                            text = message['text']
                            # Ignore messages that are ! commands
                            if text.startswith('!'):
                                continue

                            for emoji in re.findall(r'(:[a-z0-9_]+:)', text):
                                if not DEBUG: cursor.execute('INSERT INTO emoji VALUES (?)', (emoji,))

                            text = re.sub(r'[`]+[^`]+[`]+', '', text) # triple code tags
                            text = re.sub(r'<[^>]+>', '', text) # urls
                            text = re.sub(r"[^a-zA-Z':_]", ' ', text).encode('ascii','ignore') # non-alphanumerics, asciiz
                            text = re.sub(r'\s*\.\s*', '', text) # remove stray periods
                            
                            text = text.strip()
                            
                            # Spellchecker
                            if text != '':
                                words = text.split()
                                for w, word in enumerate(words):
                                    if (word not in config.word_whitelist) and (
                                            word != word.lower()) and (checker.check(word.lower())):
                                        words[w] = word.lower()
                                    
                                    if words[w] == 'i':
                                        words[w] = 'I'
                                    
                                text = ' '.join(words)

                                text = text[0].upper() + text[1:] + '. ' # capitalize
                            # print text

                            if text and not DEBUG:
                                cursor.execute('INSERT INTO message VALUES(?, ?)', (message['user'], text))
                    except Exception as e:
                        print(e)
                conn.commit()

if DEBUG: print("WARNING: WAS RUN IN DEBUG MODE; NOTHING SAVED TO DB")
