import os, sqlite3
import config

conn = sqlite3.connect(config.dbfile)
cursor = conn.cursor()

if not os.path.exists(config.dbfile):
    cursor.execute('CREATE TABLE user(nickid INTEGER PRIMARY KEY, usercode TEXT, username TEXT, permission TEXT, beer INTEGER)')
    conn.commit()

def add_new_user(usercode, username, permission='user', beers=config.starting_beers):
    cursor.execute('INSERT INTO user VALUES (NULL, ?, ?, ?, ?)', (usercode, username, permission, beers))
    conn.commit()

def get_user(usercode=None, username=None):
    if usercode:
        session.execute('SELECT * FROM user WHERE usercode=?', usercode)
    elif username:
        session.execute('SELECT * FROM user WHERE username=?', username)
