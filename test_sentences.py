import sentences

sents = [
    'The cat ran to the dog.',
    'I said that the cat ran to the dog.',
    'John fixed the vase that he broke.',
    'The cat did not run to the dog.',
    'That is a good computer.',
    'I am an awesome person.',
    'Those claims should have been being examined a lot lately.',
    'Fred may be being judged to have been deceived by the explanation.',
    "Bob's fish eats food.",
    "Food is being eaten by Bob's fish.",
    "George Washington is.",
    "George Washington is not.",
    "This is an apple computer!",
    "is.",
    "is not.",
    "eat.",
    "Under the tree lay a pride of lions.",
    "Is this an apple computer?",
    "is",
    "Bob ate the apple, while Alice ate the orange.",
    "Under the tree lay a pride of lions, and elephant slept and ate.",
    "Yesterday Donna watched a movie, cleaned her apartment and was making lunch.",
    "Yesterday Donna was happy, had watched a movie, did not clean her apartment and was making and eating lunch.",
    "I like drinking iced coffee.",
    'Fred may be being judged to have been deceived by the explanation.',
        ]

if __name__ == '__main__':
    for sent in sents:
        #print(sent)
        for s in sentences.qualify(sent):
            print(s)
        print()
