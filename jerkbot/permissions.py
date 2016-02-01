class PermissionManager(object):
    def __init__(self, filename=None):
        self.permissions = {}
        if filename:
            self.load_from_file(filename)

    def load_from_file(self, filename):
        with open(filename) as f:
            for line in f.read().splitlines():
                username, permission = line.split(':')
                self.permissions[username] = permission

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            for username, permission in self.permissions:
                f.write(username + ':' + permission)

    def get_permission_level(self, nickname):
        return self.permissions[nickname]

    def is_admin(self, nickname):
        return self.permissions[nickname] == 'admin'
