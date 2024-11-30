from Card import Card
from collections import Counter


class Hand:
    def __init__(self, face_values: str, bet: int = 0):
        self.face_values: str = face_values
        self.values: [int] = [Card.convert_face_to_value(c) for c in self.face_values]
        self.sorted_values: [int] = sorted([v for v in self.values], reverse=True)

        self.perform_joker_hack()

        self.cards: [Card] = [Card.create_from_value(v) for v in self.sorted_values]
        self.bet: int = bet
        self.combo: int = -1

    def perform_joker_hack(self):
        dic_count = Counter(self.sorted_values)
        dic_sorted = sorted(dic_count.items(), key=lambda x: x[1], reverse=True)
        highest_element = dic_sorted[0][0]
        nb_highest_element = dic_sorted[0][1]
        nb_joker = dic_count[1]

        while nb_joker:
            print(f"JOKER HACK {self.sorted_values} -> ", end="")
            joker = self.sorted_values.pop()
            idx_highest = self.sorted_values.index(highest_element)
            self.sorted_values.insert(idx_highest+nb_highest_element, joker)
            print(f"{self.sorted_values}")

            nb_joker -= 1

    def score_hand(self):
        # Start from the highest combo and test our way down
        # Test for combo "Five of a kind"
        if (self.cards[1] == self.cards[0] and
                self.cards[2] == self.cards[0] and
                self.cards[3] == self.cards[0] and
                self.cards[4] == self.cards[0]):
            self.combo = 6

        # Test for combo "Four of a kind" in this manner XXXX.
        elif (self.cards[1] == self.cards[0] and
              self.cards[2] == self.cards[0] and
              self.cards[3] == self.cards[0]):
            self.combo = 5

        # Test for combo "Four of a kind" in this manner .XXXX
        elif (self.cards[2] == self.cards[1] and
              self.cards[3] == self.cards[1] and
              self.cards[4] == self.cards[1]):
            self.combo = 5

        # Test for combo "Full house" in this manner 11122
        elif (self.cards[1] == self.cards[0] and
              self.cards[2] == self.cards[0] and
              self.cards[4] == self.cards[3]):
            self.combo = 4

        # Test for combo "Full house" in this manner 11222
        elif (self.cards[1] == self.cards[0] and
              self.cards[3] == self.cards[2] and
              self.cards[4] == self.cards[2]):
            self.combo = 4

        # Test for combo "Three of a kind" in this manner XXX..
        elif (self.cards[1] == self.cards[0] and
              self.cards[2] == self.cards[0]):
            self.combo = 3

        # Test for combo "Three of a kind" in this manner .XXX.
        elif (self.cards[2] == self.cards[1] and
              self.cards[3] == self.cards[1]):
            self.combo = 3

        # Test for combo "Three of a kind" in this manner ..XXX
        elif (self.cards[3] == self.cards[2] and
              self.cards[4] == self.cards[2]):
            self.combo = 3

        # Test for combo "Two pair" in this manner 1122.
        elif (self.cards[1] == self.cards[0] and
              self.cards[3] == self.cards[2]):
            self.combo = 2

        # Test for combo "Two pair" in this manner 11.22
        elif (self.cards[1] == self.cards[0] and
              self.cards[4] == self.cards[3]):
            self.combo = 2

        # Test for combo "Two pair" in this manner .1122
        elif (self.cards[2] == self.cards[1] and
              self.cards[4] == self.cards[3]):
            self.combo = 2

        # Test for combo "One pair" in this manner XX...
        elif self.cards[1] == self.cards[0]:
            self.combo = 1

        # Test for combo "One pair" in this manner .XX..
        elif self.cards[2] == self.cards[1]:
            self.combo = 1

        # Test for combo "One pair" in this manner ..XX.
        elif self.cards[3] == self.cards[2]:
            self.combo = 1

        # Test for combo "One pair" in this manner ...XX
        elif self.cards[4] == self.cards[3]:
            self.combo = 1
        else:
            self.combo = 0

    def __eq__(self, other):
        if self.combo < other.combo:
            return False
        elif self.combo > other.combo:
            return False
        else:
            for i in range(5):
                if self.values[i] < other.values[i]:
                    return False
                elif self.values[i] > other.values[i]:
                    return False
            else:
                return True

    def __lt__(self, other):
        if self.combo < other.combo:
            return True
        elif self.combo > other.combo:
            return False
        else:
            for i in range(5):
                if self.values[i] < other.values[i]:
                    return True
                elif self.values[i] > other.values[i]:
                    return False
            else:
                return False

    def __gt__(self, other):
        if self.combo < other.combo:
            return False
        elif self.combo > other.combo:
            return True
        else:
            for i in range(5):
                if self.values[i] < other.values[i]:
                    return False
                elif self.values[i] > other.values[i]:
                    return True
            else:
                return False

    def __le__(self, other):
        return self == other or self < other

    def __ge__(self, other):
        return self == other or self > other

    def __str__(self):
        ret_cards = ""
        for card in self.cards:
            ret_cards += card.__str__()

        return f"Hand: {self.face_values}; Bet: {self.bet}; Combo: {self.combo}; Values: {self.values}; sorted: {self.sorted_values}; Cards: {ret_cards}"
