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

        line2_data: str = line2.split(":")[1]
        records_txt: [str] = re.findall(r" \d+", line2_data)
        records: [int] = [int(n) for n in records_txt]

        return games_lengths, records

    def run(self) -> int:
        self.load_data()
        games_lengths, records = self.interpret_data()

        multiplied = 1
        for i in range(len(games_lengths)):
            max_time, record = games_lengths[i], records[i]

            sum_won_game = 0
            for x in range(max_time):
                score = self.__evaluate(x, max_time)

                if score > record:
                    sum_won_game += 1

            multiplied *= sum_won_game

        print(multiplied)
        return multiplied