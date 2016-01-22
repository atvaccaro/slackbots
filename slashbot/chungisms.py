import random

chungisms = [
    'Password.... helps.',
    'What is "one"?',
    'Yes, thank you..',
    'Oh, yes, thank you for your question...',
    'If you are found to be dishonest, you will be reported to the... proper authorities...',
    #'If you do not know this key thing, you are not software engineer...',
    'If they ask you this question in interview and you cannot answer, please do not tell them you took this class.',
    'The definition of insanity is doing the same thing over and over and expecting a new result. -Einstein',
]

def get_wisdom():
    return chungisms[random.randrange(len(chungisms))]
