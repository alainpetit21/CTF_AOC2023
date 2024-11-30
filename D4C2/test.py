import main


def test_analysis(drawn: [int], my: [int]):
    score= main.analyse_winning(drawn, my)

    assert (score == 8)


def test_game(game_text: str):
    drawn, my = main.interpret_game(game_text)

    assert (drawn[1] == 48)
    assert (my[6] == 48)

    return drawn, my


def test_line():
    hdr, game, idx = main.interpret_line(main.data[0])
    assert (hdr[0] == 'C')
    assert (game[2] == '1')
    assert (idx == 1)

    return game


def test_loading():
    data = main.load_data("example.txt")
    main.data = data

    # Should work v
    assert (data[0][0] == 'C')
    assert (data[1][8] == '1')

    # Should fail v
    # assert (data[1][0] == '6')


if __name__ == '__main__':
    test_loading()
    game = test_line()
    drawn, my = test_game(game)
    test_analysis(drawn, my)

    print("passed all tests")

