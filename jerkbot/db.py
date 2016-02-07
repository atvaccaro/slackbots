import os, sqlite3
from config import dbfile

conn = sqlite3.connect(dbfile)
cursor = conn.cursor()

if not cursor.execute('SELECT name FROM sqlite_master WHERE type="table"').fetchall():
    cursor.execute('CREATE TABLE user(nickid INTEGER PRIMARY KEY, usercode TEXT, username TEXT, permission INTEGER, beer INTEGER)')
    conn.commit()
