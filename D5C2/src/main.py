from Challenge import Challenge


def main():
    print(f'Hi, d5c1')

    challenge = Challenge("data/input.txt.bak.bak.bak")
    challenge.interpret_seeds_data()
    challenge.interpret_map_data()
    challenge.run()


if __name__ == '__main__':
    main()
