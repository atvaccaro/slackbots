import os, sqlite3
from config import dbfile

conn = sqlite3.connect(dbfile)
cursor = conn.cursor()

if not os.path.exists(dbfile):
    cursor.execute('CREATE TABLE user(nickid INTEGER PRIMARY KEY, usercode TEXT UNIQUE, username TEXT, permission INTEGER, beer INTEGER)')
    conn.commit()
