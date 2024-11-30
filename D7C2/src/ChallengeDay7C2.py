from Challenge import Challenge
from Hand import Hand


class ChallengeDay7C2(Challenge):
    def __init__(self, filename=None):
        super().__init__(filename)
        self.hands: [Hand] = []

    def interpret_data(self, data_inj: [str] = None):
        data = super().interpret_data(data_inj)

        for row in data:
            grp = row.split(" ")
            hand = grp[0]
            bet = int(grp[1])
            self.hands.append(Hand(hand, bet))

    def sort_hands(self):
        sorted_hands = []
        while len(self.hands) != 0:
            smallest = 0

            # Find smallest
            for i in range(1, len(self.hands)):
                if self.hands[i] < self.hands[smallest]:
                    smallest = i

            sorted_hands.append(self.hands[smallest])
            del self.hands[smallest]

        self.hands = sorted_hands

    def score_hands(self):
        for hand in self.hands:
            hand.score_hand()

    def calculate_winning(self):
        all_winnings = 0
        for i, hand in enumerate(self.hands):
            hand_winning = (i+1) * hand.bet
            all_winnings += hand_winning
            print(f"{hand}; hand_winning: {hand_winning}; all_winnings: {all_winnings}")

        return all_winnings

