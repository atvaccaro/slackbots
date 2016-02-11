import config
from db import cursor
import markovify

class Markov(object):
    def __init__(self, usercode):
        words = ''
        for row in cursor.execute('SELECT body FROM message WHERE usercode=?', (usercode,)):
            word = ' '.join(row[0].split()) + '. '
            word = word[0].upper() + word[1:]
            words += word

        self.text_model = markovify.Text(words)


    def generate_markov_text(self):
        return ' '.join(self.text_model.chain.walk(None))
