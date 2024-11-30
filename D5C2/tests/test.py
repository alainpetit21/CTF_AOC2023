import src.main

from src.Challenge import Challenge
from src.SpecialRegexManager import SpecialRegexManager


def test_special_regex():
    spec_reg = SpecialRegexManager([r"(seeds:)(\s\d+)+", r"^([a-z\-]+)+\smap:", r"^\n", r"^(\d+\s+)+"])

    assert (spec_reg.process("seeds: 79 14 55 13") == 0)
    assert (spec_reg.process("seeds: 432986705 28073546 1364097901 88338513 2733524843 234912494 3151642679 224376393 485709676 344068331 1560394266 911616092 3819746175 87998136 892394515 435690182 4218056486 23868437 848725444 8940450") == 0)

    assert (spec_reg.process("seed-to-soil map:") == 1)

    assert (spec_reg.process("\n") == 2)

    assert (spec_reg.process("52 50 48") == 3)
    assert (spec_reg.process("0 2377540042 17565155") == 3)


def test_loading():
    challenge = Challenge()
    data = challenge.load_data("./data/example.txt")

    # Should work v
    assert (data[0][0] == 's')
    assert (data[3][0] == '5')

    # Should fail v
    # assert (data[1][0] == '6')


def test_interpreting():
    challenge = Challenge()
    data = challenge.load_data("./data/example.txt")
    seeds = challenge.interpret_seeds_data(data)

    assert seeds[0] == 79
    assert seeds[1] == 14
    assert seeds[2] == 55
    assert seeds[3] == 13

    maps = challenge.interpret_map_data(data)

    assert maps[0].get_entry(0)[1] == 50
    assert maps[0].get_entry(0)[0] == 98
    assert maps[0].get_entry(0)[2] == 2

    assert maps[6].get_entry(1)[1] == 56
    assert maps[6].get_entry(1)[0] == 93
    assert maps[6].get_entry(1)[2] == 4


def test_sorting():
    challenge = Challenge()
    data = challenge.load_data("./data/example.txt")
    maps = challenge.interpret_map_data(data)

    for my_map in maps:
        my_map.sort()

    for my_map in maps:
        map_max = len(my_map.values)
        for n in range(map_max-1):
            assert my_map.get_entry(n)[0] <= my_map.get_entry(n+1)[0]


def test_normalization():
    challenge = Challenge()
    data = challenge.load_data("./data/example.txt")
    maps = challenge.interpret_map_data(data)

    for my_map in maps:
        my_map.sort()

    for my_map in maps:
        my_map.normalize()

    for my_map in maps:
        map_max = len(my_map.values)

        assert my_map.values[0][0] == 0
        assert my_map.values[0][2] == my_map.values[1][0]


def test_get_y():
    challenge = Challenge()
    data = challenge.load_data("./data/example.txt")
    maps = challenge.interpret_map_data(data)

    for my_map in maps:
        my_map.sort()

    for my_map in maps:
        my_map.normalize()

    assert maps[0].get_y(50) == 52
    assert maps[0].get_y(98) == 50

    assert maps[0].get_y(51) == 53
    assert maps[0].get_y(99) == 51

    assert maps[0].get_y(67) == 69
    assert maps[0].get_y(68) == 70

    assert maps[0].get_y(0) == 0
    assert maps[0].get_y(1) == 1
    assert maps[0].get_y(48) == 48
    assert maps[0].get_y(49) == 49


def test_run():
    challenge = Challenge()
    data = challenge.load_data("./data/example.txt")
    challenge.interpret_seeds_data(data)
    challenge.interpret_map_data(data)

    min_value = challenge.run()

    assert min_value == 46


if __name__ == '__main__':
    test_loading()
    test_special_regex()
    test_interpreting()
    test_sorting()
    test_normalization()
    test_get_y()
    test_run()

    print("passed all tests")

