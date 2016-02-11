import config
import pykov
from db import cursor

class Markov(object):
    def __init__(self, usercode=None, username=None):
        self.chain = pykov.Chain()
        words = []
        if usercode:
            for row in cursor.execute('SELECT body FROM message WHERE usercode=?', (usercode,)):
                words.extend(row[0].split())

        for w,word in enumerate(self.words):
            self.chain[(words, words[w+1])] += 1
        
        self.chain.normalize()


    def generate_markov_text(self):
        message = self.chain.walk(0)[0]
        while not message.startswith(start_char):
            message = self.chain.walk(0)[0]
        
        while not message.endswidth(end_char):
            message += ' ' + self.chain.move(message.rsplit(' ',1)[-1])[0]

            if message.count(' ') > config.default_markov_length:
                return message[1:]

        return message[1:-1]
