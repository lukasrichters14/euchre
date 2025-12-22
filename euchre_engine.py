from cards import *
from player import *


class EuchreEngine:

    def __init__(self, players: list[EuchrePlayer]):
        self.deck = EuchreDeck()
        self.players = players
    
    def play(self):
        print(self.deck)
        self.deck.shuffle()
        print(self.deck)

        for j, p in enumerate(self.players):
            if j % 2 == 0:
                p.pick_up(self.deck.deal())
                p.pick_up(self.deck.deal())
            else:
                p.pick_up(self.deck.deal())
                p.pick_up(self.deck.deal())
                p.pick_up(self.deck.deal())
        
        for j, p in enumerate(self.players):
            if j % 2 == 0:
                p.pick_up(self.deck.deal())
                p.pick_up(self.deck.deal())
                p.pick_up(self.deck.deal())
            else:
                p.pick_up(self.deck.deal())
                p.pick_up(self.deck.deal())
        
        for p in self.players:
            print(p.hand)
