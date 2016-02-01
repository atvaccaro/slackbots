from db import cursor

class BeerManager(object):
    def __init__(self):
        self.beers = db.get_all_beers()

    def add_beers(self, username, number_beers):
        pass

    def subtract_beers(self, username, number_beers):
        pass

    def get_all_beers():
        return cursor.execute('SELECT (usercode, beer) FROM user')

    def get_beers(user):
        return cursor.execute('SELECT (usercode, beer) FROM user WHERE usercode=?', (user))
