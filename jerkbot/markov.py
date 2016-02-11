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

    def generate_markov_text(self, size=config.default_markov_length):
        ''.join(self.chain.walk(size))
