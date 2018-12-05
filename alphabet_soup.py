#!/usr/bin/env python
# coding: utf-8
"""
 Alphabet_soup.py
 ( Heap sorting -- timing is _always_  .LE. N*loh N  )
"""

from __future__ import print_function
import sys

# { Source array, tree and result }
#WORDS = "Heap Array sorting by tree building q"
#SOUP = "qwertyuiopasdfghjklzxcvbnm   AHeerray sorting by tree building q"
WORDS = "1234"
SOUP = "1122337"
def FixTree(iFrom, iTo, elC):
    """Universal function for sorting tree and leaves."""
    elTop = elC[iFrom-1]
    while True:
        iFromTwice = iFrom*2
        if iFromTwice > iTo:
            break
        else:
            elLeft = elC[iFromTwice-1]
            if iFromTwice == iTo:
                elRight = elLeft
            else:
                elRight = elC[iFromTwice]

            if (elRight > elTop) and (elRight > elLeft):
                elC[iFrom-1] = elRight
                iFrom = iFromTwice+1
            elif elLeft > elTop:
                elC[iFrom-1] = elLeft
                iFrom = iFromTwice
            else:
                break

    elC[iFrom-1] = elTop

def main():
    """
    if you can write your message of WORDS with t
    he letters found in your bowl of SOUP
    """

# { Read unsorted array of words }
#    for (i=0;iNumA < strlen(WORDS);i++) elA[++iNumA] = (int)words[i]
    iNumA = len(WORDS)
    elA = list(WORDS)
    print("\n",elA,"\n")
# { Read unsorted array of soup }
#    for (i=0;iNumB < strlen(SOUP);i++) elB[++iNumB] = (int)soup[i]
    iNumB = len(SOUP)
    elB = list(SOUP)
    print("\n",elB,"\n")

# { Build a sorting trees }
#  for ( i= iNumA >> 1; i >=1; i--) FixTree(i,iNumA,elA)
    for i in range(int(iNumA / 2), 0, -1):
        FixTree(i, iNumA, elA)
#        print("* ", i, " ", iNumA,elA)
#  for ( i= iNumB >> 1; i >=1; i--) FixTree(i,iNumB,elB)
    for i in range(int(iNumB / 2), 0, -1):
        FixTree(i, iNumB, elB)
#        print("** ", i, " ", iNumB,elB)

# { Convert tree to array }
    for i in range(iNumA, 1, -1):
        elA[0], elA[i-1] = elA[i-1], elA[0]
        FixTree(1, i-1, elA)
        print("*-> ", iNumA, ", ", i-1,elA)

#  for (i=iNumB; i>=2; i-- )
    for i in range(iNumB, 1, -1):
        elB[0], elB[i-1] = elB[i-1], elB[0]
        FixTree(1, i-1, elB)
        print("**-> ", iNumB, ", ", i-1,elB)

# { Displey the result }
    print("* Sorted arrays *\n")
    print(iNumA, elA);
    print(iNumB, elB);



if __name__ == '__main__':
    sys.exit(main())
