import main


def test_winnings():
    data = main.load_file("./data/example.txt")
    hands = main.interpret_data()
    hands = main.score_hands(hands)
    hands = main.sort_hands(hands)
    winnings = main.calculate_winning(hands)

    assert winnings == 6440


def test_hands_sort():
    data = main.load_file("./data/example.txt")
    hands = main.interpret_data()
    hands = main.score_hands(hands)
    hands = main.sort_hands(hands)

    assert hands[0][0][0] == [13, 10, 3, 3, 2]
    assert hands[1][0][0] == [13, 11, 11, 10, 10]
    assert hands[2][0][0] == [13, 13, 7, 7, 6]
    assert hands[3][0][0] == [11, 10, 5, 5, 5]
    assert hands[4][0][0] == [14, 12, 12, 12, 11]


def test_hand_comparison():
    cards = [14, 14, 14, 14, 14]
    hand1 = ((cards, cards), 0, main.score_hand(cards))
    hand2 = ((cards, cards), 0, main.score_hand(cards))

    assert main.hand_is_equal(hand1, hand2)

    cards1 = [14, 14, 14, 14, 12]
    cards2 = [14, 14, 14, 14, 13]
    hand1 = ((cards1, cards1), 0, main.score_hand(cards1))
    hand2 = ((cards2, cards2), 0, main.score_hand(cards2))

    assert main.hand_is_smaller(hand1, hand2)
    assert main.hand_is_greater(hand2, hand1)

    cards1 = [14, 14, 14, 13, 13]
    cards2 = [14, 14, 13, 13, 13]
    hand1 = ((cards1, cards1), 0, main.score_hand(cards1))
    hand2 = ((cards2, cards2), 0, main.score_hand(cards2))

    assert main.hand_is_smaller(hand2, hand1)

    cards1 = [14, 14, 14, 13, 12]
    cards2 = [14, 14, 13, 13, 13]
    hand1 = ((cards1, cards1), 0, main.score_hand(cards1))
    hand2 = ((cards2, cards2), 0, main.score_hand(cards2))

    assert main.hand_is_smaller(hand1, hand2)

    cards1 = [14, 14, 14, 13, 12]
    cards2 = [13, 13, 14, 12, 12]
    hand1 = ((cards1, cards1), 0, main.score_hand(cards1))
    hand2 = ((cards2, cards2), 0, main.score_hand(cards2))

    assert main.hand_is_smaller(hand2, hand1)

    cards1 = [14, 14, 13, 13, 12]
    cards2 = [13, 13, 14, 12, 12]
    hand1 = ((cards1, cards1), 0, main.score_hand(cards1))
    hand2 = ((cards2, cards2), 0, main.score_hand(cards2))

    assert main.hand_is_smaller(hand2, hand1)

    cards1 = [14, 14, 10, 9, 8]
    cards2 = [14, 14, 13, 12, 11]
    hand1 = ((cards1, cards1), 0, main.score_hand(cards1))
    hand2 = ((cards2, cards2), 0, main.score_hand(cards2))

    assert main.hand_is_smaller(hand1, hand2)


def test_score_hands():
    data = main.load_file("./data/example.txt")
    hands = main.interpret_data()
    hands = main.score_hands(hands)

    assert hands[0][2] == 1
    assert hands[1][2] == 3
    assert hands[2][2] == 2
    assert hands[3][2] == 2
    assert hands[4][2] == 3


def test_score_hand():
    res = main.score_hand([14, 14, 14, 14, 14])
    assert res == 6

    res = main.score_hand([12, 10, 10, 10, 10])
    assert res == 5

    res = main.score_hand([14, 14, 14, 14, 12])
    assert res == 5

    res = main.score_hand([14, 14, 14, 12, 12])
    assert res == 4

    res = main.score_hand([14, 14, 12, 12, 12])
    assert res == 4

    res = main.score_hand([14, 14, 14, 12, 11])
    assert res == 3

    res = main.score_hand([14, 13, 13, 13, 11])
    assert res == 3

    res = main.score_hand([14, 13, 12, 12, 12])
    assert res == 3

    res = main.score_hand([14, 14, 13, 13, 12])
    assert res == 2

    res = main.score_hand([14, 14, 13, 12, 12])
    assert res == 2

    res = main.score_hand([14, 13, 13, 12, 12])
    assert res == 2

    res = main.score_hand([14, 14, 13, 12, 11])
    assert res == 1

    res = main.score_hand([14, 13, 13, 12, 11])
    assert res == 1

    res = main.score_hand([14, 13, 12, 12, 11])
    assert res == 1

    res = main.score_hand([14, 13, 12, 11, 11])
    assert res == 1

    res = main.score_hand([14, 13, 12, 11, 10])
    assert res == 0


def test_interpret_data():
    data = main.load_file("./data/example.txt")
    hands = main.interpret_data()

    assert hands[0][0][0][0] == 13
    assert hands[0][1] == 765
    assert hands[4][0][0][1] == 12


def test_convert_poker_numbering():
    assert main.convert_poker_number('A') == 14
    assert main.convert_poker_number('6') == 6


def test_loading():
    main.data = main.load_file("./data/example.txt")

    assert main.data[0][1] == '2'
    assert main.data[4][4] == 'A'


if __name__ == '__main__':
    test_loading()
    test_convert_poker_numbering()
    test_interpret_data()
    test_score_hand()
    test_hand_comparison()
    test_score_hands()
    test_hands_sort()
    test_winnings()

    print("Passed all tests")
