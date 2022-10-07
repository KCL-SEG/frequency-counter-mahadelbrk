"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):

    frequencies={}
    counts = dict()
    for i in items:
        counts[i] = str(counts.get(i, 0) + 1)

    return counts
    # from collections import Counter

    # c = Counter(items) 

    # newItem= (Counter(items))
    # return 
