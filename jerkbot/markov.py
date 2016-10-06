import config
from db import cursor
from markovify import markovify

userlist = {}
for row in cursor.execute('SELECT usercode, username FROM user'):
    userlist[row[0]] = row[1]
markov_chains = {}
print userlist

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


def imitate(username):
    try:
        usercode = [key for key, value in userlist.items() if value == username.replace('@', '')][0]
    except IndexError:
        return 'Error: unknown or missing user'

    if usercode not in markov_chains:
        markov_chains[usercode] = Markov(usercode)

    message = markov_chains[usercode].generate_markov_text()
    return message
