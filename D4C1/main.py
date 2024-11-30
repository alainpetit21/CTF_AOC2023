import re

data = []


# This function will only load the data as 2D array and return it so that it can be used and address later
def load_data(filename: str) -> [[chr]]:
    with open(filename, "r") as file_in:
        rows = file_in.readlines()

    return rows


# This function will interpret the line and break it down into hdr : game text and index humber
def interpret_line(txt_line: str) -> (str, str, int):
    group_hdr_game = txt_line.split(':')
    game_hdr = group_hdr_game[0]
    game_text = group_hdr_game[1]

    # remove the extra spaces in the game header
    elements = re.findall(r'([a-zA-Z]*)\s*([0-9]*)', game_hdr)
    game_hdr = " ".join(elements[0])

    # The game text will stay formatted for now, interpret_game will take care of that

    idx = int(game_hdr.split(' ')[1])
    return game_hdr, game_text, idx


# This function will interpret the game text and extract all number and organize them in 2 lists : drawn number and
# my own number
def interpret_game(txt_game: str) -> ([int], [int]):
    group_game = txt_game.split('|')
    game_drawn_text = group_game[0]
    game_my_text = group_game[1]

    # extract the spacing in drawn numbers
    elements = re.findall(r'\d+', game_drawn_text)
    game_drawn_text = elements

    # and convert them into numbers
    game_drawn = []
    for str_num in game_drawn_text:
        game_drawn.append(int(str_num))

    # extract the spacing in my numbers
    elements = re.findall(r'\d+', game_my_text)
    game_my_text = elements

    game_my = []
    for str_num in game_my_text:
        game_my.append(int(str_num))

    return game_drawn, game_my


# This function is responsible to calculate the score for the lists of numbers (drawn and my own)
def analyse_winning(drawn: [int], my: [int]) -> int:

    score = 0
    for win_num in drawn:
        if win_num in my:
            score += 1

    if score > 0:
        return 2**(score-1)
    else:
        return 0


# This is the main function, where we do the main high level logic of the algorithm
def main():
    global data
    print(f'Hi, d4c1')

    # Get the data from the file, organize in list of string
    data = load_data("input.txt")
    # data = load_data("example.txt")

    sum_score = 0
    for line in data:

        # break down each line in hdr, game text and extract its index
        _, game, idx = interpret_line(line)

        # break down game text into drawn numbers and my own numbers
        drawn, my = interpret_game(game)

        # for each line and all the list of drawn number and my numder analysi the score for this line
        score = analyse_winning(drawn, my)

        # Sum up and print
        sum_score += score
        print(f" Card {idx}: score : {score}")

    # Final output
    print(f" Total score : {sum_score}")


if __name__ == '__main__':
    main()
