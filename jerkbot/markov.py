import config
from db import cursor
from markovify import markovify


class Markov(object):
    def __init__(self, usercode):
        message_history = ''
        messages = [row[0] for row in cursor.execute('SELECT body FROM message WHERE usercode=?', (usercode,))]
        self.text_model = markovify.Text('. '.join(messages))


    def generate_markov_text(self):
        output = ''
        for r in range(config.markov_sentences):
            attempts = 0
            sentence = ' '.join(self.text_model.chain.walk(None))
            while attempts < 100 and len(sentence.split()) < config.markov_sentence_length:
                sentence = ' '.join(self.text_model.chain.walk(None))
                attempts += 1

            sentence = sentence.replace('.', '').strip()
            output += sentence + '. '

        return output[:-1]

if __name__ == '__main__':
    markov = Markov('U09F9MTNW')
    message = markov.generate_markov_text()
    print(message)
