import os, sqlite3
import config

conn = sqlite3.connect(config.dbfile)
cursor = conn.cursor()

if not os.path.exists(config.dbfile):
    cursor.execute('CREATE TABLE user(nickid INTEGER PRIMARY KEY, usercode TEXT, username TEXT, permission TEXT, beer INTEGER)')
    conn.commit()
