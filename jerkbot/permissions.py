from db import cursor

class PermissionManager(object):
    def __init__(self):
        self.permissions = {}
        self.load_from_db():

    def load_from_db(self):
        all_permissions = db.get_all_permissions()
        for row in all_permissions:
            self.permissions[row[0]] = row[1]

    def save_to_db(self):
        for usercode,permission in permissions.iteritems():
            db.update_permission(usercode, permissions)

    def get_permission_level(self, usercode):
        return self.permissions[usercode]

    def is_admin(self, usercode):
        return self.permissions[usercode] == 'admin'

    def get_all_permissions():
        return cursor.execute('SELECT (usercode, permission) FROM user')

    def update_permission(usercode, permission):
        cursor.execute('UPDATE user SET permission=? WHERE usercode=?', (permission, usercode))
