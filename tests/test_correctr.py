#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from correctr import correct


class TestCorrectr:

    def test_repeated_characters(self):
        assert correct('sheeeeeep') == 'sheep'
        assert correct('jjoobbb') == 'job'
        assert correct('peepple') == 'people'

    def test_vowels(self):
        assert correct('weke') == 'wake'

    def test_no_correction_found(self):
        assert correct('sheeple') == False

    def test_case_sensitivity(self):
        assert correct('inSIDE') == 'inside'

    def test_combined(self):
        assert correct('CUNsperrICY') == 'conspiracy'

    def test_randomized(self, random_word, expected):
        assert correct(random_word) == expected
