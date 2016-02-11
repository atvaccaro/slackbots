import re, sys, os
import config
from db import cursor
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import markovify.markovify

class Markov(object):
    def __init__(self, usercode):
        message_history = ''
        for row in cursor.execute('SELECT body FROM message WHERE usercode=?', (usercode,)):
            sentence = re.sub(r'\s', ' ', row[0])
            if not sentence.endswith('.'):
                sentence += '. '
            sentence = sentence[0].upper() + sentence[1:]
            message_history += sentence

        self.text_model = markovify.Text(message_history)


    def generate_markov_text(self):
        output = ''
        for r in range(config.markov_sentences):
            output += ' '.join(self.text_model.chain.walk(None)) + ' '
        return output[:-1]
