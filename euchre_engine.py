from cards import *
from player import *


class EuchreEngine:

    def __init__(self, players: list[EuchrePlayer]):
        self.deck = EuchreDeck()
        self.players = players
    
    def deal_hand(self, dealer: int):
        self.deck.shuffle()

        for i in range(len(self.players)):
            idx = (dealer + i + 1) % len(self.players)
            p = self.players[idx]

            if idx % 2 == 0:
                p.pick_up(self.deck.deal())
                p.pick_up(self.deck.deal())
            else:
                p.pick_up(self.deck.deal())
                p.pick_up(self.deck.deal())
                p.pick_up(self.deck.deal())
        
        for i in range(len(self.players)):
            idx = (dealer + i + 1) % len(self.players)
            p = self.players[idx]

            if idx % 2 == 0:
                p.pick_up(self.deck.deal())
                p.pick_up(self.deck.deal())
                p.pick_up(self.deck.deal())
            else:
                p.pick_up(self.deck.deal())
                p.pick_up(self.deck.deal())

    
    def play(self):
        dealer = 0
        self.deal_hand(dealer)
        bid_trump = self.deck.deal()
        print(bid_trump)
        
