from engine.Exceptions.ExFileNotProvided import ExFileNotProvided
from engine.Exceptions.ExNoData import ExNoData


class Challenge:
    def __init__(self, filename=None):
        self.__filename = filename

        if self.__filename is not None:
            self.data = self.load_data(self.__filename)

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

    def interpret_data(self, data_inj: [str] = None):
        if data_inj is not None:
            data = self.data = data_inj
        elif self.data is not None:
            data = self.data
        else:
            raise ExNoData()

        return data

    def run(self):
        pass
