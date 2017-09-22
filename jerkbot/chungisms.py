import random

chungisms = [
    'Password... helps.',
    'What is "one"?',
    'Yes, thank you...',
    'Softgoal interdependency graph...',
    'Security is CIA: confidentiality, integrity, and accessibility.'
    'Oh, yes, thank you for your question...',
    'If you are found to be dishonest, you will be reported to the... proper authorities...',
    'If they ask you this question in interview and you cannot answer, please do not tell them you took this class.',
    'The definition of insanity is doing the same thing over and over and expecting a new result. -Einstein',
    'The use of the "man-hour" implies that Rome can be built in a day.',
    '_repeated inhalation laughter_',
    'At Harvard business school, the classes are very interactive and the students actively participate.',
    'All boys liking Mary does not imply Mary likes all boys.',
    'Your work demonstrates a deep understanding of requirements engineering.',
    # 'If you do not know this key thing, you are not software engineer...',
]


def get_wisdom():
    return random.choice(chungisms)
