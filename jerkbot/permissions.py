import db
from db import cursor

USER = 0
MODERATOR = 1
ADMIN = 2
SUPERADMIN = 3

def save_to_db():
    for usercode,permission in permissions.iteritems():
        update_permission(usercode, permissions)

def get_permission(usercode):
    return permissions[usercode]

def is_admin(usercode):
    return permissions[usercode] >= ADMIN

def get_all_permissions():
    return cursor.execute('SELECT usercode, permission FROM user')

def update_permission(usercode, permission):
    permissions[usercode] = permission
    cursor.execute('UPDATE user SET permission=? WHERE usercode=?', (permission, usercode))

permissions = {}
for row in get_all_permissions():
    permissions[row[0]] = row[1]
