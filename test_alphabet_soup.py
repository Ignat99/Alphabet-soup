#/usr/bin/env python
# coding: utf-8

"""
Test Alphabet soup.
"""

from __future__ import print_function
import pytest
import alphabet_soup as als
import os
import sys

#WORDS = "Heap Array sorting by tree building q"
#SOUP = "qwertyuiopasdfghjklzxcvbnm   AHeerray sorting by tree building q"
WORDS = "123589"
SOUP = "11223358"

def test_numbers_3_4():
#    assert als.main(WORDS,SOUP) == True
    print("test 3*4")
    assert 3*4 == 12

@pytest.mark.parametrize('words', ['123', '12345', '123999'])
@pytest.mark.parametrize('soup', ['999912345', '11922993345', '444555911223399'])
def test_main(words, soup):
    assert als.main(words,soup)


@pytest.mark.parametrize('words', ['12349', '123455', '123999'])
@pytest.mark.parametrize('soup', ['123', '11223345', '11223399'])
def test_main_false(words, soup):
    assert als.main(words,soup) == False
