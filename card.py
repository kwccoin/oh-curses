class Card:
    rank_values = {
        "2"  : 2,
        "3"  : 3,
        "4"  : 4,
        "5"  : 5,
        "6"  : 6,
        "7"  : 7,
        "8"  : 8,
        "9"  : 9,
        "10" : 10,
        "J"  : 11,
        "Q"  : 12,
        "K"  : 13,
        "A"  : 14
    }

    suit_ascii = {
        "clubs"    : '♣',
        "diamonds" : '♦',
        "spades"   : '♠',
        "hearts"   : '♥'
    }

    colors = {
        "spades"   : 0,
        "hearts"   : 1,
        "clubs"    : 2,
        "diamonds" : 4
    }

    def __init__(self, rank: str, suit: str):
        assert(rank in self.rank_values)
        self.rank = rank
        self.value = self.rank_values[rank]
        assert(suit in self.suit_ascii)
        self.suit = suit
        self.visible = False

    def show(self):
        self.visible = True

    def hide(self):
        self.visible = False

    def color(self) -> int:
        return self.colors[self.suit]

    def trick_value(self, led_suit, trump_suit) -> int:
        if (self.suit == trump_suit):
            return 100 + self.value
        if (self.suit == led_suit):
            return self.value
        return 0

    # # sorry, this was a good idea, but I had no idea how to pass in globals
    # def __lt__(self, other):
    #     assert(Globals.trump_suit and Globals.led_suit)
    #     if self.__class__ == other.__class__:
    #         if (self.suit == Globals.trump_suit):
    #             if (other.suit == Globals.trump_suit):
    #                 return self.value < other.value
    #             else:
    #                 return False
    #         elif (other.suit == Globals.trump_suit):
    #             return True
    #         elif (self.suit == Globals.led_suit):
    #             if (other.suit == Globals.led_suit):
    #                 return self.value < other.value
    #             else:
    #                 return False
    #         elif (other.suit == Globals.led_suit):
    #             return True
    #         else:
    #             return False
    #     return NotImplemented

    # def __eq__(self, other):
    #     assert(Globals.trump_suit and Globals.led_suit)
    #     if self.__class__ == other.__class__:
    #         if (self.suit != Globals.trump_suit and self.suit != Globals.led_suit and
    #             other.suit != Globals.trump_suit and other.suit != Globals.trump_suit):
    #             return True
    #         else:
    #             return False
    #     return NotImplemented

    def __repr__(self):
        return "{:s}{:s}".format(self.rank, self.suit_ascii[self.suit])

    def ascii_rep(self) -> str:
        if (self.visible):
            return (
                "\
┌─────────┐\n\
│{}       │\n\
│         │\n\
│         │\n\
│    {}   │\n\
│         │\n\
│         │\n\
│       {}│\n\
└─────────┘\
                ".format(
                    format(self.rank, ' <2'),
                    format(self.suit_ascii[self.suit], ' ^2'),
                    format(self.rank, ' >2'),
                    )
                )
        else:
            return (
                "\
┌─────────┐\n\
│░░░░░░░░░│\n\
│░░░░░░░░░│\n\
│░░░░░░░░░│\n\
│░░░░░░░░░│\n\
│░░░░░░░░░│\n\
│░░░░░░░░░│\n\
│░░░░░░░░░│\n\
└─────────┘\
")

# testing card
if __name__ == "__main__":
    c = Card("K", "clubs")
    d = Card("10", "diamonds")
    print(c.ascii_rep())
    c.set_visible()
    d.set_visible()
    print(c.ascii_rep())
    print(d.ascii_rep())
