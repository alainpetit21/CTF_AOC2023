from Card import Card
from Hand import Hand
from src.ChallengeDay7C2 import ChallengeDay7C2


def test_loading():
    chall = ChallengeDay7C2("./data/example2.txt")

    assert chall.data[0][1] == '3'
    assert chall.data[4][4] == '3'


def test_convert_poker_numbering():
    assert Card.convert_face_to_value('A') == 13
    assert Card.convert_face_to_value('6') == 6
    assert Card.convert_face_to_value('J') == 1


def test_interpret_data():
    chall = ChallengeDay7C2("./data/example.txt")
    chall.interpret_data()

    assert chall.hands[0].cards[0] == Card.create_from_face('K')
    assert chall.hands[0].bet == 765
    assert chall.hands[4].cards[1] == Card.create_from_face('Q')


def test_score_hand():
    hand = Hand("KKKKK")
    hand.score_hand()
    assert hand.combo == 6

    hand = Hand("QTTTT")
    hand.score_hand()
    assert hand.combo == 5

    hand = Hand("KKKKQ")
    hand.score_hand()
    assert hand.combo == 5

    hand = Hand("AAAQQ")
    hand.score_hand()
    assert hand.combo == 4

    hand = Hand("AAQQQ")
    hand.score_hand()
    assert hand.combo == 4

    hand = Hand("AAAQT")
    hand.score_hand()
    assert hand.combo == 3

    hand = Hand("AKKKT")
    hand.score_hand()
    assert hand.combo == 3

    hand = Hand("AKQQQ")
    hand.score_hand()
    assert hand.combo == 3

    hand = Hand("AAKKQ")
    hand.score_hand()
    assert hand.combo == 2

    hand = Hand("AAKQQ")
    hand.score_hand()
    assert hand.combo == 2

    hand = Hand("AKKQQ")
    hand.score_hand()
    assert hand.combo == 2

    hand = Hand("AAKQT")
    hand.score_hand()
    assert hand.combo == 1

    hand = Hand("AKKQT")
    hand.score_hand()
    assert hand.combo == 1

    hand = Hand("AKQQT")
    hand.score_hand()
    assert hand.combo == 1

    hand = Hand("AKQTT")
    hand.score_hand()
    assert hand.combo == 1

    hand = Hand("AKQT9")
    hand.score_hand()
    assert hand.combo == 0


def test_hand_comparison():
    hand1 = Hand("AAAAA")
    hand2 = Hand("AAAAA")
    hand1.score_hand()
    hand2.score_hand()
    assert hand1 == hand2

    hand1 = Hand("AAAAQ")
    hand2 = Hand("AAAAK")
    hand1.score_hand()
    hand2.score_hand()
    assert hand1 < hand2
    assert hand2 > hand1

    hand1 = Hand("AAKKK")
    hand2 = Hand("AAAKK")
    hand1.score_hand()
    hand2.score_hand()
    assert hand1 < hand2

    hand1 = Hand("AAAKQ")
    hand2 = Hand("AAKKK")
    hand1.score_hand()
    hand2.score_hand()
    assert hand1 < hand2

    hand1 = Hand("AAAKQ")
    hand2 = Hand("AAKKK")
    hand1.score_hand()
    hand2.score_hand()
    assert hand1 < hand2

    hand1 = Hand("AAAKQ")
    hand2 = Hand("AKKQQ")
    hand1.score_hand()
    hand2.score_hand()
    assert hand2 < hand1

    hand1 = Hand("AAKKQ")
    hand2 = Hand("AKKQQ")
    hand1.score_hand()
    hand2.score_hand()
    assert hand2 < hand1

    hand1 = Hand("AAT98")
    hand2 = Hand("AAKQT")
    hand1.score_hand()
    hand2.score_hand()
    assert hand1 < hand2


def test_score_hands():
    chall = ChallengeDay7C2("./data/example.txt")
    chall.interpret_data()
    chall.score_hands()

    assert chall.hands[0].combo == 1
    assert chall.hands[1].combo == 5
    assert chall.hands[2].combo == 2
    assert chall.hands[3].combo == 5
    assert chall.hands[4].combo == 5


def test_hands_sort():
    chall = ChallengeDay7C2("./data/example.txt")
    chall.interpret_data()
    chall.score_hands()
    chall.sort_hands()

    hand1 = Hand("32T3K")
    hand2 = Hand("KK677")
    hand3 = Hand("T55J5")
    hand4 = Hand("QQQJA")
    hand5 = Hand("KTJJT")

    hand1.score_hand()
    hand2.score_hand()
    hand3.score_hand()
    hand4.score_hand()
    hand5.score_hand()

    assert chall.hands[0] == hand1
    assert chall.hands[1] == hand2
    assert chall.hands[2] == hand3
    assert chall.hands[3] == hand4
    assert chall.hands[4] == hand5


def test_winnings():
    chall = ChallengeDay7C2("./data/example.txt")
    chall.interpret_data()
    chall.score_hands()
    chall.sort_hands()
    winnings = chall.calculate_winning()
    assert winnings == 5905

    chall = ChallengeDay7C2("./data/example2.txt")
    chall.interpret_data()
    chall.score_hands()
    chall.sort_hands()
    winnings = chall.calculate_winning()
    assert winnings == 6839

    chall = ChallengeDay7C2("./data/example3.txt")
    chall.interpret_data()
    chall.score_hands()
    chall.sort_hands()
    winnings = chall.calculate_winning()
    assert winnings == 7460


def test_edges():
    hand1 = Hand("2233J")
    hand1.score_hand()
    assert hand1.combo == 4

    hand2 = Hand("AJJ23")
    hand2.score_hand()
    assert hand2.combo == 3

    hand3 = Hand("KKK23")
    hand3.score_hand()
    assert hand3.combo == 3

    hand4 = Hand("A2223")
    hand4.score_hand()
    assert hand4.combo == 3

    assert hand3 < hand2
    assert hand2 < hand4

    hand = Hand("234JJ")
    hand.score_hand()
    assert hand.combo == 3

    hand = Hand("JKQKK")
    hand.score_hand()
    assert hand.combo == 5


if __name__ == '__main__':
    test_loading()
    test_convert_poker_numbering()
    test_interpret_data()
    test_score_hand()
    test_hand_comparison()
    test_score_hands()
    test_hands_sort()
    test_winnings()
    test_edges()

    print("Passed all tests")
