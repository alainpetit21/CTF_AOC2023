import re


# Turned the challenge into an object IOT prevent global variable
class D4C2:
    def __init__(self):
        # This one will contain all raw text of the card
        self.data: [str] = []

        # This one will contain all card in a format of  list of tupples
        # (consisted of card#, array of drawn number, array of my number)
        self.cards: [(int, [int], [int])] = []

        # This one will contain all card currently being processed, same format as above
        self.processing: [(int, [int], [int])] = []

    # This function is responsible to calculate the score for the lists of numbers (drawn and my own)
    def analyse_winning(self, drawn: [int], my: [int]) -> int:
        score = 0
        for win_num in drawn:
            if win_num in my:
                score += 1

        return score

    # This function will interpret the game text and extract all number and organize them in 2 lists : drawn number and
    # my own number
    def interpret_game(self, txt_game: str) -> ([int], [int]):
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

    # This function will interpret the line and break it down into hdr : game text and index humber
    def interpret_line(self, txt_line: str) -> (str, str, int):
        group_hdr_game = txt_line.split(':')
        game_hdr = group_hdr_game[0]
        game_text = group_hdr_game[1]

        # remove the extra spaces in the game header
        elements = re.findall(r'([a-zA-Z]*)\s*([0-9]*)', game_hdr)
        game_hdr = " ".join(elements[0])

        # The game text will stay formatted for now, interpret_game will take care of that

        idx = int(game_hdr.split(' ')[1])
        return game_hdr, game_text, idx


    # This function will only load the data as 2D array and return it so that it can be used and address later
    def load_data(self, filename: str) -> [[chr]]:
        with open(filename, "r") as file_in:
            rows = file_in.readlines()

        return rows


# This is the main function, where we do the main high level logic of the algorithm
def main():
    print(f'Hi, d4c1')

    # Basic initialization
    challenge = D4C2()
    challenge.data = challenge.load_data("input.txt.bak.bak.bak.bak.bak2.bak")
    # challenge.data = challenge.load_data("example.txt")

    # Build the initial cards array
    sum_score = 0
    for line in challenge.data:
        _, game, idx = challenge.interpret_line(line)
        drawn, my = challenge.interpret_game(game)

        challenge.cards.append((idx-1, drawn, my))

    # All cards will be processed
    challenge.processing = [card for card in challenge.cards]

    # Phase 2 process the cards, be aware that depending on the score, more cards will be added to this LIFO list
    idx = 0
    while idx < len(challenge.processing):
        card_id, drawn, my = challenge.processing[idx]
        nb_matches = challenge.analyse_winning(drawn, my)

        if nb_matches > 0:
            print(f" Card {idx} is a winner with score : {nb_matches}", end="")

            for i in range(card_id+1, card_id+1+nb_matches):
                card_id, drawn_to_add, my_to_add = challenge.processing[i]
                challenge.processing.append((card_id, drawn_to_add, my_to_add))
                print(f" adding Card {i}, ", end="")

            print()
        idx += 1

    print(f" Total number of card  : {len(challenge.processing)}")


if __name__ == '__main__':
    main()
