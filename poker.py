import random

suits = ["♠", "♥", "♦", "♣"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]


class Card(object):
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def __str__(self):
        return "%s%s" % (self.rank, self.suit)


class Deck(object):
    def __init__(self):
        self.cards = []
        for s in suits:
            for r in ranks:
                self.cards.append(Card(s, r))

    def shuffle(self):
        random.shuffle(self.cards)

    def __str__(self):
        deck = ""
        for i in range(0, 52):
            deck += str(self.cards[i]) + " "
        return deck

    def take_one(self):
        return self.cards.pop(0)


class Hand(object):
    def __init__(self, deck):
        self.cards = []
        for i in range(5):
            self.cards.append(deck.take_one())

    def __str__(self):
        hand = ""
        for i in range(5):
            hand += str(self.cards[i]) + " "
        return hand

    def is_pair(self):
        for i in range(5):
            for j in range(i + 1, 5):
                if self.cards[i].get_rank() == self.cards[j].get_rank():
                    return True
        return False

    def is_royal_flush(self):
        c = ["10", "J", "Q", "K", "A"]
        suit = self.cards[0].get_suit()
        for card in self.cards:
            if card.get_suit() != suit:
                return False
            suit = card.get_suit()
            if card.get_rank() not in c:
                return False
        return True

    def is_royal_flush(self):
        position = ranks.index(self.cards[0].get_rank())
        suit = self.cards[0].get_suit()
        for card in self.cards[1:]:
            if card.get_suit() != suit:
                return False
            position += 1
            if ranks.index(self.cards[0].get_rank()) != position:
                return False
        return True

    def is_four_of_a_kind(self):
        d = {}
        for card in self.cards:
            rank = card.get_rank()
            if rank in d:
                d[rank] += 1
            else:
                d[rank] = 1
        for i in d.keys:
            if d[i] == 4:
                return True
        return False

    def is_full_house(self):
        d = {}
        for card in self.cards:
            rank = card.get_rank()
            if rank in d:
                d[rank] += 1
            else:
                d[rank] = 1
        if len(d) == 2:
            two, three = 0, 0
            for i in d.keys():
                if d[i] == 3:
                    three = True
                if d[i] == 2:
                    two = True
            if two and three:
                return True
        return False

    def is_flush(self):
        suit = self.cards[0].get_suit()
        for card in self.cards[1:]:
            if card.get_suit() != suit:
                return False
        return False

    def is_straight(self):
        position = ranks.index(self.cards[0].get_rank())
        for card in self.cards[1:]:
            position += 1
            if ranks.index(card.get_rank()) != position:
                return False
        return True

    def is_three_of_a_kind(self):
        d = {}
        for card in self.cards:
            rank = card.get_rank()
            if rank in d:
                d[rank] += 1
            else:
                d[rank] = 1
        for i in d.keys:
            if d[i] == 3:
                return True
        return False

    def is_two_pairs(self):
        d = {}
        for card in self.cards:
            rank = card.get_rank()
            if rank in d:
                d[rank] += 1
            else:
                d[rank] = 1
        pairs = 0
        for i in d.keys:
            if d[i] == 2:
                pairs += 1
        if pairs == 2:
            return True
        return False

    def is_pair(self):
        d = {}
        for card in self.cards:
            rank = card.get_rank()
            if rank in d:
                d[rank] += 1
            else:
                d[rank] = 1
        for i in d.keys:
            if d[i] == 2:
                return True
        return False

    def high_card(self):
        position = ranks.index(self.cards[0].get_rank())
        card = self.cards[0].get_rank()
        for card in self.cards[1:]:
            if ranks.index(card.get_rank()) > position:
                card = card.get_rank()
                position = ranks.index(self.cards[0].get_rank())
        return card


new_deck = Deck()
new_deck.shuffle()
print(new_deck)
hand = Hand(new_deck)
print(hand)