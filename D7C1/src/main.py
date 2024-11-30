# only the string of text loaded from the file
data: [str] = []
hands: [(([int], [int]), int, int)] = []     #once interpretted, list of hands, which are tuple of hand, bet, and scored_combo


def calculate_winning(all_hands: [(([int], [int]), int, int)]) -> [(([int], [int]), int, int)]:
    global hands

    all_winnings = 0
    for i, hand in enumerate(all_hands):
        all_winnings += (i+1) * hand[1]
        print(hand)

    return all_winnings


def sort_hands(all_hands: [(([int], [int]), int, int)]) -> [(([int], [int]), int, int)]:
    global hands

    sorted_hands = []

    while len(all_hands) != 0:
        smallest = 0

        # Find smallest
        for i in range(1, len(all_hands)):
            if hand_is_smaller(all_hands[i], all_hands[smallest]):
                smallest = i

        sorted_hands.append(all_hands[smallest])
        del all_hands[smallest]

    hands = sorted_hands
    return sorted_hands


def hand_is_greater(left: (([int], [int]), int, int), right: (([int], [int]), int, int)) -> bool:
    if hand_is_equal(left, right):
        return False
    elif hand_is_smaller(left, right):
        return False
    else:
        return True


def hand_is_equal(left: (([int], [int]), int, int), right: (([int], [int]), int, int)) -> bool:
    if left[2] < right[2]:
        return False
    elif left[2] > right[2]:
        return False
    else:
        for i in range(5):
            if left[0][1][i] < right[0][1][i]:
                return False
            elif left[0][1][i] > right[0][1][i]:
                return False
        else:
            return True


def hand_is_smaller(left: (([int], [int]), int, int), right: (([int], [int]), int, int)) -> bool:
    if left[2] < right[2]:
        return True
    elif left[2] > right[2]:
        return False
    else:
        for i in range(5):
            if left[0][1][i] < right[0][1][i]:
                return True
            elif left[0][1][i] > right[0][1][i]:
                return False
        else:
            return False


def score_hand(cards: [int]) -> int:
    combo = -1

    # Start from the highest combo and test our way down
    if cards[0] == cards[1] and cards[1] == cards[2] and cards[2] == cards[3] and cards[3] == cards[4]:
        combo = 6
    elif cards[0] == cards[1] and cards[1] == cards[2] and cards[2] == cards[3]:
        combo = 5
    elif cards[1] == cards[2] and cards[2] == cards[3] and cards[3] == cards[4]:
        combo = 5
    elif (cards[0] == cards[1] and cards[1] == cards[2]) and (cards[3] == cards[4]):
        combo = 4
    elif (cards[0] == cards[1]) and (cards[2] == cards[3] and cards[3] == cards[4]):
        combo = 4
    elif cards[0] == cards[1] and cards[1] == cards[2]:
        combo = 3
    elif cards[1] == cards[2] and cards[2] == cards[3]:
        combo = 3
    elif cards[2] == cards[3] and cards[3] == cards[4]:
        combo = 3
    elif cards[0] == cards[1] and cards[2] == cards[3]:
        combo = 2
    elif cards[0] == cards[1] and cards[3] == cards[4]:
        combo = 2
    elif cards[1] == cards[2] and cards[3] == cards[4]:
        combo = 2
    elif cards[0] == cards[1]:
        combo = 1
    elif cards[1] == cards[2]:
        combo = 1
    elif cards[2] == cards[3]:
        combo = 1
    elif cards[3] == cards[4]:
        combo = 1
    else:
        combo = 0

    return combo


def score_hands(all_hands: [(([int], [int]), int, int)]) -> [(([int], [int]), int, int)]:
    global hands

    hands = []
    for i, hand in enumerate(all_hands):
        all_hands[i] = ((hand[0][0], hand[0][1]), hand[1], score_hand(hand[0][0]))

    hands = all_hands
    return hands


def load_file(filename: str) -> [str]:
    global data

    with open(filename, "r") as file:
        data = file.readlines()

    return data


def convert_poker_number(c: chr) -> int:
    if c == 'A':
        return 14
    elif c == 'K':
        return 13
    elif c == 'Q':
        return 12
    elif c == 'J':
        return 11
    elif c == 'T':
        return 10
    elif c == '9':
        return 9
    elif c == '8':
        return 8
    elif c == '7':
        return 7
    elif c == '6':
        return 6
    elif c == '5':
        return 5
    elif c == '4':
        return 4
    elif c == '3':
        return 3
    elif c == '2':
        return 2


def interpret_data() -> [(([int], [int]), int)]:
    global data
    global hands

    hands = []
    for line in data:
        grp = line.split(" ")
        hand = grp[0]
        bet = int(grp[1])

        hand_values = [convert_poker_number(c) for c in hand]
        hand_values_sorted = sorted([convert_poker_number(c) for c in hand], reverse=True)

        hands.append(((hand_values_sorted, hand_values), bet))

    return hands


def main():
    global data
    global hands
    print(f'Hi, d7c1')

    data = load_file("./data/input.txt")
    hands = interpret_data()
    hands = score_hands(hands)
    hands = sort_hands(hands)
    winnings = calculate_winning(hands)

    print(winnings)


if __name__ == '__main__':
    main()
