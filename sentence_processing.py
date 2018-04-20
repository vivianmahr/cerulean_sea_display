SWBD_DAMSL_SIMPLE = {
    "questions": {
        "qo": "open-ended question",
        "qr": "'or' question",
        "qw": "wh-question",
        "qy": "yes or no question"
    },
    "statement": {
        "s": "statement"
    },
    "protocols": {
        "fa": "apology",
        "fc": "fc",
        "fp": "opening or greeting",
        "ft": "thanks",
        "fw": "welcome"
    },
    "other": {
        "o": "other"
    }
}

COMMANDS = {
    "special commands": '''Phrases  I look for:
     "special commands"
     "who made you"
     "libraries used"
     "future plans"''',
    
    "who made you": 'You can contact the person who made me at vivianmahr@gmail.com.',
    
    "libraries used": "I was made using Spacy to process the languages, Django as a server, and Angular to handle the frontend. Hm, if I grow enough to be considered an AI, would I be bilingual?",

    "future plans": "Next, my creator wants me to start learning to split text by utterances for dialogue tagging. I plan to stop using SWBD-DAMSL and start using DiAML."
}


def categorize_sentence(sentence):
    sentence = sentence.lower()
    special = is_special_case(sentence)
    if special[0]:
        return special
    
def is_special_case(sentence):
    for command in COMMANDS.keys():
        if command in sentence:
            return (True, COMMANDS[command])
    return tuple([False, -1])

