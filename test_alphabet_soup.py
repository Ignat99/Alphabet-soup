#/usr/bin/env python
# coding: utf-8

"""
Test Alphabet soup.
"""

from __future__ import print_function
import pytest
import alphabet_soup as als


#WORDS = "Heap Array sorting by tree building q"
#SOUP = "qwertyuiopasdfghjklzxcvbnm   AHeerray sorting by tree building q"
WORDS = "123589"
SOUP = "11223358"

@pytest.mark.parametrize('words', ['123', '12345', '123999'])
@pytest.mark.parametrize('soup', \
    ['999912345', '11922993345', '444555911223399'])
def test_main(words, soup):
    """Test for True cases"""
    assert als.main(words, soup)


@pytest.mark.parametrize('words', ['12349', '123455', '123999'])
@pytest.mark.parametrize('soup', ['123', '11223345', '11223399'])
def test_main_false(words, soup):
    """Test for False cases"""
    assert als.main(words, soup) == False
