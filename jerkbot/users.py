import config, permissions
from db import cursor

class UserManager(object):
    def __init__(self):
        self.users = {}
        for row in cursor.execute('SELECT usercode,username FROM user'):
            self.users[row[0]] = row[1]

    def get_all_users(self):
        return self.users

    def save_all_users(self):
        for usercode,username in self.users.iteritems():
            self.add_or_update_user(usercode, username)

    def add_user(self, usercode, username, permission=permissions.USER, beers=config.starting_beers):
        cursor.execute('INSERT INTO user VALUES (NULL, ?, ?, ?, ?)', (usercode, username, permission, beers))
        conn.commit()

    def get_user(self, usercode=None, username=None):
        if not usercode and not username:
            raise ValueError('Must give either usercode or username')
        elif usercode:
            return cursor.execute('SELECT * FROM user WHERE usercode=?', usercode)
        else:
            return cursor.execute('SELECT * FROM user WHERE username=?', username)
