import collections

def print_separator():
    print('\n')
    print('======================================================================================================')
    print('\n')
    

Card = collections.namedtuple('Card',['rank','suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
        
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]

print_separator()

beer_card = Card('7','diamonds')
print(beer_card)

frenchDeck = FrenchDeck()

print_separator()

print('Print number of cards with dunder len: \n')
print(len(frenchDeck))

print_separator()
print('Print with dunder getitem: \n')
print(frenchDeck[15])

print_separator()
print('Print with choice module: \n')
from random import choice

print(choice(frenchDeck))

print_separator()
print('Because our delegates to the operator of cards, our deck auto __getitem__ [] self._cards, automatically supports slicing: \n')
print(frenchDeck[:3])

print_separator()
print('Just by implementing the __getitem__ special method, our deck is also iterable: \n')

for card in frenchDeck:
    print(card)

print('\n')
print('Also reversed: \n')

for card in reversed(frenchDeck):
    print(card)

print_separator()
print('For sorting we can define a sort function: \n')

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(frenchDeck, key=spades_high):
    print(card)
    
print_separator()
