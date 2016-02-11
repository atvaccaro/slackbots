import config
import pykov
from db import cursor

class Markov(object):
    def __init__(self, usercode):
        self.chain = pykov.Chain()
        words = []
        for row in cursor.execute('SELECT body FROM message WHERE usercode=?', (usercode,)):
                words.extend(row[0].split())
        for w,word in enumerate(words):
            self.chain[(words, words[w+1])] += 1

        self.chain.normalize()


<<<<<<< HEAD
    def generate_markov_text(self, size=config.default_markov_length):
        ''.join(self.chain.walk(size))
=======
    def generate_markov_text(self):
        message = self.chain.walk(0)[0]
        while not message.startswith(start_char):
            message = self.chain.walk(0)[0]

        while not message.endswidth(end_char):
            message += ' ' + self.chain.move(message.rsplit(' ',1)[-1])[0]

            if message.count(' ') > config.default_markov_length:
                return message[1:]

        return message[1:-1]
>>>>>>> 54d5c4b67e42541229c1d1a340f6fc2e0391e02e
