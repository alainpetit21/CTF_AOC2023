from typing import Tuple


# This function's role will be interpreted the string of a single draw and return the sample in dict format
def interpret_one_draw(draw_text: str) -> dict[str, int]:
    draw_sample = {"red": 0, "green": 0, "blue": 0}

    components = draw_text.split(', ')

    for component in components:
        group_num_col = component.split(' ')
        num = int(group_num_col[0])
        color = group_num_col[1]

        draw_sample[color] = num

    print(f'R: {draw_sample["red"]}, G: {draw_sample["green"]}, B: {draw_sample["blue"]} -|||- ', end="")
    return draw_sample


# This function's role will be interpreted the game and return the power of the minimum in the game
def interpret_game(game_text: str) -> int:
    draw_min_game = {"red": 0, "green": 0, "blue": 0}
    draws = game_text.split('; ')

    for draw in draws:
        ret = interpret_one_draw(draw)
        draw_min_game["red"] = max(draw_min_game["red"], ret["red"])
        draw_min_game["green"] = max(draw_min_game["green"], ret["green"])
        draw_min_game["blue"] = max(draw_min_game["blue"], ret["blue"])

    mult = draw_min_game["red"] * draw_min_game["green"] * draw_min_game["blue"]

    print(f"Min: R:{draw_min_game['red']}; G:{draw_min_game['green']}; B:{draw_min_game['blue']} = Mult: {mult}", end="")
    return mult


# This function interpret the whole line in break it down by component for interpreting the game and returning the power
# of the minimum for that line
def interpret_line(line_text: str) -> int:
    group_hdr_game = line_text.split(': ')
    game_hdr = group_hdr_game[0]
    game_text = group_hdr_game[1]
    idx = int(game_hdr.split(' ')[1])

    return interpret_game(game_text)


# This is the main function, where we do the file manipulation and the main sum of index if return is negative
def main():
    print(f'Hi, World')

    sum_ret = 0

    # with open("example.txt", "r") as inputFile:
    with open("input.txt", "r") as inputFile:
        lines = inputFile.readlines()

        for line in lines:
            ret = interpret_line(line[:-1])

            sum_ret += ret
            print(f': sum:{sum_ret}')

    print(f"sum_idx: {sum_ret}")


if __name__ == '__main__':
    main()
