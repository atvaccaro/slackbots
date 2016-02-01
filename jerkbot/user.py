from db import cursor

class UserManager(object):
    def __init__(self):
        self.users = {}
        for row in get_all_users():
            users[row[0]] = row[1]
            
    def get_all_users():
        for row in cursor.execute('SELECT * FROM user'):


    def add_new_user(usercode, username, permission='user', beers=config.starting_beers):
        cursor.execute('INSERT INTO user VALUES (NULL, ?, ?, ?, ?)', (usercode, username, permission, beers))
        conn.commit()

    def get_user(usercode=None, username=None):
        if not usercode and not username:
            raise ValueError('Must give either usercode or username')
        elif usercode:
            return cursor.execute('SELECT * FROM user WHERE usercode=?', usercode)
        else:
            return cursor.execute('SELECT * FROM user WHERE username=?', username)
