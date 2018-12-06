#!/usr/bin/env python
# coding: utf-8
"""
 Alphabet_soup.py
 ( Heap sorting -- timing is _always_  .LE. N*loh N  )
"""

from __future__ import print_function
import sys

#WORDS = "Heap Array sorting by tree building q"
#SOUP = "qwertyuiopasdfghjklzxcvbnm   AHeerray sorting by tree building q"
WORDS = "123"
SOUP = "112233"

def fix_tree(i_from, i_to, el_c):
    """Universal function for sorting tree and leaves."""
    el_top = el_c[i_from-1]
    while True:
        i_from_twice = i_from*2
        if i_from_twice > i_to:
            break
        else:
            el_left = el_c[i_from_twice-1]
            if i_from_twice == i_to:
                el_right = el_left
            else:
                el_right = el_c[i_from_twice]

            if (el_right > el_top) and (el_right > el_left):
                el_c[i_from-1] = el_right
                i_from = i_from_twice+1
            elif el_left > el_top:
                el_c[i_from-1] = el_left
                i_from = i_from_twice
            else:
                break

    el_c[i_from-1] = el_top

# { Source arrays, trees and result }
def main(words, soup):
    """
    if you can write your message of WORDS with t
    he letters found in your bowl of SOUP
    """

# { Read unsorted array of words }
    i_num_a = len(words)
    el_a = list(words)

# { Read unsorted array of soup }
    i_num_b = len(soup)
    el_b = list(soup)


# { Build a sorting trees }
    for i in range(i_num_a // 2, 0, -1):
        fix_tree(i, i_num_a, el_a)


    for i in range(i_num_b // 2, 0, -1):
        fix_tree(i, i_num_b, el_b)


# { Convert tree to array }
    for i in range(i_num_a, 1, -1):
        el_a[0], el_a[i-1] = el_a[i-1], el_a[0]
        fix_tree(1, i-1, el_a)


    for i in range(i_num_b, 1, -1):
        el_b[0], el_b[i-1] = el_b[i-1], el_b[0]
        fix_tree(1, i-1, el_b)


# { Displey the result }
    print("* Sorted arrays *")
    print(i_num_a, el_a)
    print(i_num_b, el_b)

    i = 1
    j = 1
    while i <= i_num_a and j <= i_num_b:
        if j <= i_num_b and el_a[i-1] > el_b[j-1]:
            j += 1

        if j <= i_num_b and el_a[i-1] < el_b[j-1]:
            print("False1")
            return False
        if j > i_num_b:
            print("False3")
            return False
        if (j <= i_num_b) and el_a[i-1] == el_b[j-1]:
            if (j == i_num_b) and (i == i_num_a):
                print("True1")
                return True
            if (j == i_num_b) and (i < i_num_a):
                print("False4")
                return False
            elif  (i < i_num_a) and (el_a[i] < el_b[j]):
                print("False2")
                return False
            elif (i < i_num_a) and (j < i_num_b) and (el_a[i] >= el_b[j]):
                i += 1
                j += 1
            else:
                i += 1

            if i > i_num_a:
                print("True2")
                return True




if __name__ == '__main__':
    sys.exit(main(WORDS, SOUP))
