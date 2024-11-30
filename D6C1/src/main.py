from Challenge import Challenge


def main():
    print(f'Hi, d6c1')
    challenge = Challenge("./data/input.txt")
    challenge.load_data()
    challenge.run()


if __name__ == '__main__':
    main()
