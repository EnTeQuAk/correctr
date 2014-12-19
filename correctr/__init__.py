# -*- coding: utf-8 -*-
import os
import cmd
import re
import itertools
import pkg_resources
import unicodedata
from textblob import Word


fname = pkg_resources.resource_filename('correctr', 'en-spelling.txt')

with open(fname) as fobj:
    WORDS = set([line.split()[0] for line in fobj])


VOWELS = u'aeiou'


def normalize(word):
    normalized = unicodedata.normalize('NFKD', word.lower())
    return normalized


def correct(word):
    word = normalize(word)

    if word in WORDS:
        return word

    # Correct repeated characters
    word = re.sub(r'(.)\1\1+', r'\1\1', word)

    if word in WORDS:
        return word

    # More aggressive word simplification. TODO: find a better way to do this.
    # There are words that are correct with repeated characters and some are
    # absolutely not. E.g It seems that `TextBlob` spellcheck does not find
    # the corrected version of `conspirricy` if those repeated "r" are in there.
    # Real search engines like Woosh or Xapian are way better in that regard.
    word = ''.join(ch for ch, _ in itertools.groupby(word))

    # check for incorrect vowels
    vowel_locations = [index for index in range(len(word)) if word[index] in VOWELS]
    vowel_permutations = itertools.product(VOWELS, repeat=len(vowel_locations))

    for permutation in vowel_permutations:
        tmp = ''
        vowel_index = 0
        for index in range(len(word)):
            if word[index] in VOWELS:
                tmp += permutation[vowel_index]
                vowel_index += 1
            else:
                tmp += word[index]

        if tmp in WORDS:
            return tmp

    # Correcting the hard way if we did not find an easy solution.
    corrected = Word(word).spellcheck()

    if corrected and corrected[0][1] >= .9:
        return corrected[0][0]

    return False


class SpellingCorrector(cmd.Cmd):
    prompt = '> '
    intro = 'Simple spelling corrector. To quit, hit ctrl+d\n\n'

    def default(self, line):
        corrected = correct(line)
        if corrected:
            print(corrected)
        else:
            print('NO SUGGESTION')

    def do_EOF(self, line):
        return True


def main():
    app = SpellingCorrector()
    app.cmdloop()


if __name__ == '__main__':
    main()
