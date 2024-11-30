import re

from ExFileNotProvided import ExFileNotProvided
from ExNoData import ExNoData




class Challenge:
    def __init__(self, filename= None):
        self.__filename = filename

        if self.__filename is not None:
            self.data = self.load_data(self.__filename)

    def __evaluate(self, button_pressed, duration_game):
        speed = button_pressed
        time_left = (duration_game - button_pressed)
        distance = (time_left * speed)
        return distance

    def load_data(self, name_input: str = None) -> [str]:
        if name_input is not None:
            filename = self.__filename = name_input
        elif self.__filename is not None:
            filename = self.__filename
        else:
            raise ExFileNotProvided()

        with open(filename, "r") as file:
            self.data = file.readlines()
            return self.data

    def interpret_data(self, data_inj: [str] = None) -> [str]:
        if data_inj is not None:
            data = self.data = data_inj
        elif self.data is not None:
            data = self.data
        else:
            raise ExNoData()

        line1:str = data[0]
        line2:str = data[1]

        line1_data: str = line1.split(":")[1]
        game_length_txt: [str] = re.findall(r" \d+", line1_data)
        games_lengths: [int] = [int(n) for n in game_length_txt]
        game_length_txt: [str] = [str(n) for n in games_lengths]
        game_length_txt: str = "".join(game_length_txt)
        game_length = int(game_length_txt)

        line2_data: str = line2.split(":")[1]
        records_txt: [str] = re.findall(r" \d+", line2_data)
        records: [int] = [int(n) for n in records_txt]
        records_txt: [str] = [str(n) for n in records]
        record_txt: str = "".join(records_txt)
        record = int(record_txt)

        return game_length, record

    def run(self) -> int:
        self.load_data()
        game_length, record = self.interpret_data()

        sum_won_game = 0
        for x in range(game_length):
            score = self.__evaluate(x, game_length)

            if score > record:
                sum_won_game += 1

            if x % 1000000 == 0:
                print(f"Evaluate {x} out of {game_length}: {(x*100) // game_length}% completed")

        print(sum_won_game)
        return sum_won_game
