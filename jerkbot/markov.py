import re, sys, os, pickle
import config
from db import cursor
sys.path.insert(1, os.path.join(sys.path[0], '../markovify'))
import markovify
from datetime import datetime

class Markov(object):
    def __init__(self, usercode):
        message_history = ''
        for row in cursor.execute('SELECT body FROM message WHERE usercode=?', (usercode,)):
            # Remove whitespace
            sentence = re.sub(r'\s+', ' ', row[0]).strip()
            # Remove any stray periods, and surrounding whitespace
            sentence = re.sub(r'\s*\.\s*', '', sentence)
            # Capitalize and add punctuation
            if sentence != '':
                sentence = sentence[0].upper() + sentence[1:] + '. '
                message_history += sentence
        self.text_model = markovify.Text(message_history)


    def generate_markov_text(self):
        output = ''
        for r in range(config.markov_sentences):
            sentence = ' '.join(self.text_model.chain.walk(None))
            sentence = sentence.replace('.', '').strip()
            output += sentence + '. '
        return output[:-1]
