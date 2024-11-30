from typing import Tuple

max_pop = {"red": 12, "green": 13, "blue": 14}


# This function will perform the actual tests if the sample is possible
def is_draw_possible(nb_red: int, nb_green: int, nb_blue: int):
    if nb_red > max_pop["red"]:
        return False
    elif nb_green > max_pop["green"]:
        return False
    elif nb_blue > max_pop["blue"]:
        return False

    return True


# This function's role will be interpreted the string of a single draw and return the sample in dict format
def interpret_one_draw(draw_text: str) -> bool:
    draw_sample = {"red": 0, "green": 0, "blue": 0}

    components = draw_text.split(', ')

    for component in components:
        group_num_col = component.split(' ')
        num = int(group_num_col[0])
        color = group_num_col[1]

        draw_sample[color] = num

    print(f'red: {draw_sample["red"]}, green: {draw_sample["green"]}, blue: {draw_sample["blue"]}; ', end="")
    return is_draw_possible(draw_sample["red"], draw_sample["green"], draw_sample["blue"])


# This function's role will be interpreted the game and return whether one of its draw is impossible.
def interpret_game(game_text: str) -> bool:
    draws = game_text.split('; ')

    for draw in draws:
        ret = interpret_one_draw(draw)

        if not ret:
            print(f': impossible!!!!', end="")
            return False

    return True


# This function interpret the whole line in break it down by component for interpreting the game and returning whether
# it is possible
def interpret_line(line_text: str) -> tuple[bool, int]:
    group_hdr_game = line_text.split(': ')
    game_hdr = group_hdr_game[0]
    game_text = group_hdr_game[1]
    idx = int(game_hdr.split(' ')[1])

    return interpret_game(game_text), idx


# This is the main function, where we do the file manipulation and the main sum of index if return is negative
def main():
    print(f'Hi, World')

    sum_idx = 0

    with open("input.txt", "r") as inputFile:
        lines = inputFile.readlines()

        for line in lines:
            ret, idx = interpret_line(line[:-1])

            if ret:
                sum_idx += idx
                print(f': index: {idx}, sum:{sum_idx}')
            else:
                print()

    print(f"sum_idx: {sum_idx}")


if __name__ == '__main__':
    main()
