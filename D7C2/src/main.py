from ChallengeDay7C2 import ChallengeDay7C2


def main():
    chall = ChallengeDay7C2("./data/input.txt")
    chall.interpret_data()
    chall.score_hands()
    chall.sort_hands()
    winnings = chall.calculate_winning()

    print(winnings)


if __name__ == '__main__':
    main()
