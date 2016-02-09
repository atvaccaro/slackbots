import random, config
from db import cursor

class Markov(object):
    def __init__(self, usercode=None, username=None):
        self.cache = {}
        self.words = []
        if usercode:
            for row in cursor.execute('SELECT body FROM message WHERE usercode=?', (usercode,)):
                self.words.extend(row[0].split())
        self.word_size = len(self.words)
        self.database()

    def doubles(self):
        if len(self.words) < 3:
            return

        for i in range(len(self.words) - 1):
            yield (self.words[i], self.words[i+1])

    def database(self):
        for w1, w2 in self.doubles():
            key = (w1)
            if key in self.cache:
                self.cache[key].append(w2)
            else:
                self.cache[key] = [w2]

    def generate_markov_text(self, size=config.default_markov_length):
        seed = random.randint(0, self.word_size-2)
        seed_word = self.words[seed]
        w1 = seed_word
        gen_words = []
        for i in xrange(size):
            gen_words.append(w1)
            w1 = random.choice(self.cache[(w1)])
        gen_words.append(w1)
        return ' '.join(gen_words)
