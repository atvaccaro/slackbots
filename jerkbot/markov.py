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


    def generate_markov_text(self, size=config.default_markov_length):
        gen_words = self.chain.walk(size)
        return ' '.join(gen_words)
