from Challenge import Challenge


def main():
    print(f'Hi, d5c1')

    challenge = Challenge("input.txt")
    challenge.interpret_seeds_data()
    challenge.interpret_map_data()
    challenge.run()


if __name__ == '__main__':
    main()
