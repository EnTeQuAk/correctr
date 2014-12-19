import random

CANDIDATES = [
    'observing', 'batiste', 'antagonizing', 'sculpture', 'robespierre',
    'privations', 'mania', 'communities', 'jollification',
    'vegetable', 'actinomyces', 'levers', 'centred',
    'scenario', 'bourbons', 'blankets', 'joint', 'squadron', 'unconquerable',
    'admiring', 'discredit', 'alongside', 'hillside',
    'teasing', 'venus', 'telescope', 'intestine', 'dmitrov',
    'unorganized', 'dosage', 'heavers', 'markets', 'convent', 'baronet', 'postpone',
    'lances', 'moving', 'reverse', 'keratomata', 'allegedly', 'chlorine', 'murdering',
    'cleaving', 'repaid', 'bordermen', 'cartilaginous', 'profound', 'emerges', 'afterward',
    'environs', 'swiftness', 'discrete', 'superb', 'lauck', 'refuse', 'tinsel',
    'clothed', 'minuit', 'softly', 'purposely', 'bower', 'confederated',
    'insanely', 'impertinent', 'humorously', 'cadaverous', 'baser', 'democrats', 'manifestoes',
    'completeness', 'universe', 'fatigues', 'skiagrams', 'faulty', 'subtracted', 'thickened',
    'inwardly', 'raisuli', 'rebuking', 'unexposed', 'kochubey', 'whitening', 'abdicated',
    'trainer', 'especially', 'confrontation', 'vigorously', 'dresden', 'paradoxical'
]

def generate_words():
    test_words = set()

    for idx, word in enumerate(CANDIDATES):
        if len(word) < 5:
            continue

        for _ in range(random.randint(1, 10)):
            if idx % 3:
                # Add repeated characters
                test_words.add((word, ''.join([char * random.randint(0, 3) or char for char in word])))
            elif idx % 5:
                # Randomize fowels
                test_words.add((word, word.translate(str.maketrans('aei', 'iea'))))
            elif idx % 7:
                test_words.add((
                    word,
                    ''.join(random.choice((str.upper, str.lower))(char) for char in word)
                ))
            elif idx % 9:
                x = ''.join([char * random.randint(0, 3) or char for char in x])
                x = x.translate(str.maketrans('aei', 'iea'))
                x = ''.join(random.choice((str.upper, str.lower))(char) for char in x)
                test_words.add(x)
            else:
                test_words.add((word, word))

    return test_words


def pytest_generate_tests(metafunc):
    if 'random_word' in metafunc.fixturenames:
        metafunc.parametrize('random_word,expected', (
            (word, expected) for expected, word in generate_words()
        ))
