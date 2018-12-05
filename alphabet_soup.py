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
WORDS = "123"
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
    iNumA = len(WORDS)
    elA = list(WORDS)

# { Read unsorted array of soup }
    iNumB = len(SOUP)
    elB = list(SOUP)


# { Build a sorting trees }
    for i in range(int(iNumA / 2), 0, -1):
        FixTree(i, iNumA, elA)


    for i in range(int(iNumB / 2), 0, -1):
        FixTree(i, iNumB, elB)


# { Convert tree to array }
    for i in range(iNumA, 1, -1):
        elA[0], elA[i-1] = elA[i-1], elA[0]
        FixTree(1, i-1, elA)


    for i in range(iNumB, 1, -1):
        elB[0], elB[i-1] = elB[i-1], elB[0]
        FixTree(1, i-1, elB)


# { Displey the result }
    print("* Sorted arrays *\n")
    print(iNumA, elA);
    print(iNumB, elB);

    i = 1
    j = 1
    while i <= iNumA:
        if elA[i-1] > elB[j-1]:
            j += 1

        print("i: ", i, ", j: ", j)
        print("elA[i]: ", elA[i-1], ", elB[j]: ", elB[j-1])

#        if i > iNumA:
#            print("\nTrue2\n")
#            return True



        if elA[i-1] < elB[j-1]:
            print("\nFalse1\n")
            return False
        if j > iNumB:
            print("\nFalse3\n")
            return False
        if elA[i-1] == elB[j-1]: #and (i < iNumA):
            if (i < iNumA) and (elA[i] < elB[j]):
                print("\nFalse2\n")
                return False
            elif (i < iNumA) and (elA[i] >= elB[j]):
                i += 1
                j += 1
            else:
                i += 1


#            print("End2 i: ", i, ", j: ", j)
#            print("End2 elA[i]: ", elA[i-1], ", elB[j]: ", elB[j-1])


            if i > iNumA:
                print("\nTrue2\n")
                return True

#        else:
#            i += 1



if __name__ == '__main__':
    sys.exit(main())
