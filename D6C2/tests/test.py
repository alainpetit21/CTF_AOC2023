from src.Challenge import Challenge


def test_run():
    challenge = Challenge()
    data = challenge.load_data("./data/example.txt")
    challenge.interpret_data(data)

    ret = challenge.run()
    assert ret == 71503


def test_interpret_data():
    challenge = Challenge()
    data = challenge.load_data("./data/example.txt")
    game_length, record = challenge.interpret_data(data)

    assert game_length == 71530
    assert record == 940200


def test_loading():
    try:
        challenge = Challenge()
        data = challenge.load_data("./data/example.txt")

        assert data[0][0] == 'T'
        assert data[1][2] == 's'

    except FileNotFoundError:
        assert False


def main():
    print(f'Hi, test for d6c2')

    test_loading()
    test_interpret_data()
    test_run()

    print("all tests passed")


if __name__ == '__main__':
    main()
