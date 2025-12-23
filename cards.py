import random


class Suit:
    SPADE = 0
    CLUB = 1
    DIAMOND = 2
    HEART = 3


class Card:

    def __init__(self, suit: int, rank: int):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        r = str(self.rank)
        if self.rank == 1:
            r = 'A'
        elif self.rank == 11:
            r = 'J'
        elif self.rank == 12:
            r = 'Q'
        elif self.rank == 13:
            r = 'K'
        elif self.rank == 0:
            r = '$'
        
        if self.suit == 0:
            s = '♠'
        elif self.suit == 1:
            s = '♣'
        elif self.suit == 2:
            s = '♦'
        elif self.suit == 3:
            s = '♥'

        return f"{r}{s}"
    
    __repr__ = __str__
    

class EuchreDeck:
    def __init__(self):
        self.deck = []
        for s in [Suit.SPADE, Suit.CLUB, Suit.DIAMOND, Suit.HEART]:
            for r in range(9, 14):
                self.deck.append(Card(s, r))
    
    def shuffle(self, n: int = 1):
        for _ in range(n):
            random.shuffle(self.deck)
    
    def deal(self) -> Card:
        return self.deck.pop()
    
    def __str__(self):
        return str(self.deck)
    
    __repr__ = __str__