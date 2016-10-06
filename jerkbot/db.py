import os, sqlite3
from config import dbfile

conn = sqlite3.connect(dbfile)
cursor = conn.cursor()

if not cursor.execute('SELECT name FROM sqlite_master WHERE type="table"').fetchall():
    cursor.execute('CREATE TABLE user(usercode TEXT, username TEXT, permission INTEGER, beers INTEGER)')
    cursor.execute('CREATE TABLE message(usercode TEXT, body TEXT)')
    cursor.execute('CREATE TABLE emoji(body TEXT)')
    conn.commit()
