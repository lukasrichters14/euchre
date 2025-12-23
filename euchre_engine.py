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

    
    def get_left_bower(self, trump: Card):
        if trump.suit == Suit.SPADE:
            return Suit.CLUB
        elif trump.suit == Suit.CLUB:
            return Suit.SPADE
        elif trump.suit == Suit.DIAMOND:
            return Suit.HEART
        elif trump.suit == Suit.HEART:
            return Suit.DIAMOND
    

    def is_new_high_card(c, high_card, trump_suit, lead_suit):
        left_bower = get_left_bower(trump_suit)

        # A card that is not tump and not following suit cannot win
        if c.suit != trump_suit and c.suit != lead_suit:
            return False
        
        # Any trump card will beat any other non-trump card
        elif c.suit == trump_suit and high_card.suit != trump_suit:
            return True
        
        # Opposite of above
        elif c.suit != trump_suit and high_card.suit == trump_suit:
            return False
        
        # Both cards are trump, use standard card values with Jacks high
        elif c.suit == trump_suit and high_card.suit == trump_suit:
            pass
        
        # Same suit, not trump, use standard card values
        else: # c1.suit == c2.suit and c1.suit != trump_suit:
            pass

    def get_best_card(self, trump_suit: int, cards: list[Card]):
        highest_card = cards[0]
        card_idx = 0
        for i in range(1, len(cards)):
            card = cards[i]
            if highest_card.suit == trump_suit and card.suit == trump_suit:
                if card.rank > highest_card.rank:
                    pass

    
    def play(self):
        dealer = 0
        self.deal_hand(dealer)
        bid_trump = self.deck.deal()
        print(bid_trump)

        left_bower = self.get_left_bower(bid_trump)
        print(left_bower)


        
        
