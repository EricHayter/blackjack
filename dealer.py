import random
from collections import Counter
from itertools import product, repeat

from card import Card
from rank import Rank
from suit import Suit


def iter_sample_fast(iterable, samplesize):
    results = []
    iterator = iter(iterable)
    # Fill in the first samplesize elements:
    try:
        for e in iterable:
            results.append(e)
    except StopIteration:
        raise ValueError("Sample larger than population.")
    random.shuffle(results)  # Randomize their positions
    for i, v in enumerate(iterator, samplesize):
        r = random.randint(0, i)
        if r < samplesize:
            results[r] = v  # at a decreasing rate, replace random items
    return results


class Dealer:
    def __init__(self, num_decks=6):
        deck = [] 

# create a iterable for a deck
deck = [Card(r, s) for r,s in  (product(list(Rank), list(Suit)))]


for i in range(1):
    c = repeat(deck, 6)
    print(iter_sample_fast(c, 1))

    




