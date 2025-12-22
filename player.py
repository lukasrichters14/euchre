from cards import *


class EuchrePlayer:

    def __init__(self, id: int):
        self.hand = []
        self.id = id
    
    def pick_up(self, card: Card):
        self.hand.append(card)
    
    def play(self, i: int):
        return self.hand.pop(i)
    
    def __str__(self):
        return str(self.hand)
    
    __repr__ = __str__
