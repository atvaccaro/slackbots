import re, sys, os
import enchant
import config
from db import cursor
sys.path.insert(1, os.path.join(sys.path[0], '../markovify'))
import markovify

class Markov(object):
    def __init__(self, usercode):
        checker = enchant.Dict('en_US')
        message_history = ''
        for row in cursor.execute('SELECT body FROM message WHERE usercode=?', (usercode,)):
            # Remove whitespace
            sentence = re.sub(r'\s+', ' ', row[0]).strip()
            # Remove any stray periods, and surrounding whitespace
            sentence = re.sub(r'\s*\.\s*', '', sentence)

            # Capitalize and add punctuation
            if sentence != '':
                words = sentence.split()
                for w, word in enumerate(words):
                    if (word not in config.word_whitelist) and (
                        word != word.lower()) and (checker.check(word.lower())):
                        words[w] = word.lower()

                sentence = ' '.join(words)

                sentence = sentence[0].upper() + sentence[1:] + '. '
                message_history += sentence

        self.text_model = markovify.Text(message_history)


    def generate_markov_text(self):
        output = ''
        for r in range(config.markov_sentences):
            sentence = ' '.join(self.text_model.chain.walk(None))
            while len(sentence.split()) < config.markov_sentence_length:
                sentence = ' '.join(self.text_model.chain.walk(None))

            sentence = sentence.replace('.', '').strip()
            output += sentence + '. '

        return output[:-1]
