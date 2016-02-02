from db import cursor

class Permission(Enum):
    USER = 0
    MODERATOR = 1
    ADMIN = 2
    SUPERADMIN = 3

class PermissionManager(object):
    def __init__(self):
        self.permissions = {}
        for row in self.get_all_permissions():
            self.permissions[row[0]] = row[1]

    def save_to_db(self):
        for usercode,permission in permissions.iteritems():
            self.update_permission(usercode, permissions)

    def get_permission(self, usercode):
        return self.permissions[usercode]

    def is_admin(self, usercode):
        return self.permissions[usercode] >= Permission.ADMIN

    def get_all_permissions():
        return cursor.execute('SELECT (usercode, permission) FROM user')

    def update_permission(usercode, permission):
        self.permissions[usercode] = permission
        cursor.execute('UPDATE user SET permission=? WHERE usercode=?', (permission, usercode))
