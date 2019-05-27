from .card import Card
from random import shuffle

class GameBoard:

    def __init__(self, players = ["Isaac", "Alex", "Ben", "Owen"]):
        shuffle(players) # decides dealer
        self.deck = [Card(rank, suit) for suit in Card.suit_ascii for rank in Card.rank_values]
        self.players = players
        self.in_play = dict()
        self.hands = {player:[] for player in self.players}
        self.bids = dict()
        self.cards_taken = {player:[] for player in self.players}
        self.trump_card = None
        self.led_suit = None

    # collect all cards back into deck
    # just reinitializes everything
    def collect_cards(self):
        self.deck = [Card(rank, suit) for suit in Card.suit_ascii for rank in Card.rank_values]
        self.in_play = {}
        self.hands = {player:[] for player in self.players}
        self.bids = dict()
        self.cards_taken = {player:[] for player in self.players}
        self.trump_card = None
        self.led_suit = None

    # deals the specified hand
    def deal_hand(self, hand_num: int):
        print("Dealing hand...", end = "")
        # can only deal from a full deck
        assert(len(self.deck) == 52)
        shuffle(self.deck)

        for player in self.players:
            for _ in range(hand_num):
                self.hands[player].append(self.deck.pop())
        if (hand_num < 13):
            self.trump_card = self.deck[0]
        print("trump card is", self.trump_card)

    # assigns a bid to a player
    def bid(self, player: str, bid: int):
        print("Player", player, "bids", bid)
        assert(player not in self.bids)
        self.bids[player] = bid

    # put a card from a specifed player into play
    def play_card(self, player: str, card: Card, lead = False):
        # can only play a card if it's in your hand
        assert(card in self.hands[player])
        # player must not have already played a card
        assert(player not in self.in_play)
        print("Playing card", card, "from player", player, "(trick lead)" if lead else "")
        if (lead):
            assert(self.led_suit is None)
            self.led_suit = card.suit

        self.in_play[player] = card
        self.hands[player].remove(card)

    # calculate the winner of the trick,
    # update trick piles, and
    # clear in_play
    def finish_trick(self) -> str:
        print("Finishing trick")
        # everyone must have played a card
        for player in self.in_play:
            assert(self.in_play[player] is not None)

        # calculate winner
        winner = max(self.in_play, key=lambda x: Card.trick_value(self.in_play[x], self.led_suit, self.trump_card.suit))
        print("Winner is", winner)
        # move cards in play to the winner's pile
        self.cards_taken[winner].extend(self.in_play.values())
        # clear the cards in play
        self.in_play = {}
        self.led_suit = None
        return winner

    def finish_hand(self):
        print("Finishing hand")
        for player in self.hands:
            assert(self.hands[player] == [])

class ClientBoard:

    def __init__(self, players, active):
        self.players = players
        self.active = active
        self.active_position = players.index(active)
        self.hands = {player:[] for player in players}
        self.won = {player:0 for player in players}
        self.in_play = dict()
        self.bids = dict()
        self.trump_card = None

    def get_hand(self, dealt_hand):
        for player in self.hands.keys():
            if player == self.active:
                self.hands[player] = [Card(card[0], card[1]) for card in dealt_hand]
                for card in self.hands[player]:
                    card.show()
            else:
                self.hands[player] = [Card() for card in dealt_hand]


# this logic will eventually go in server.py
if __name__ == "__main__":
    g = GameBoard()
    g.deal_hand(2)
    print("hands now are ", g.hands)
    for _ in range(2):
        print("playing trick")
        g.play_card(g.players[0], g.hands[g.players[0]][0], lead = True)
        g.play_card(g.players[1], g.hands[g.players[1]][0])
        g.play_card(g.players[2], g.hands[g.players[2]][0])
        g.play_card(g.players[3], g.hands[g.players[3]][0])
        print("hands now are ", g.hands)
        print("in play now is ", g.in_play)
        g.finish_trick()
        print("in play now is ", g.in_play)
        print("cards taken now are", g.cards_taken)
    g.finish_hand()

