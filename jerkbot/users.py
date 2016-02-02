import config
from db import cursor

class NameManager(object):
    def __init__(self)  :
        self.users = {}
        for row in self.get_all_users():
            users[row[1]] = row[2]

    def get_all_users():
        return cursor.execute('SELECT * FROM user')

    def save_all_users():
        for usercode,username in self.users.iteritems():
            self.add_or_update_user(usercode, username)

    def add_user(usercode, username, permission=Permission.USER, beers=config.starting_beers):
        cursor.execute('INSERT INTO user VALUES (NULL, ?, ?, ?, ?)', (usercode, username, permission, beers))
        conn.commit()

    def get_user(usercode=None, username=None):
        if not usercode and not username:
            raise ValueError('Must give either usercode or username')
        elif usercode:
            return cursor.execute('SELECT * FROM user WHERE usercode=?', usercode)
        else:
            return cursor.execute('SELECT * FROM user WHERE username=?', username)
