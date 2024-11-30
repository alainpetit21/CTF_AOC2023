import re

from MapX2Y import MapX2Y
from SpecialRegexManager import SpecialRegexManager


class Challenge:
    def __init__(self, filename_input = None):
        self.rows = []
        self.lst_seeds = []
        self.lst_maps = []
        self.lst_location = []

        if filename_input is not None:
            self.rows = self.load_data(filename_input)

    # This function will only load the data as 2D array and return it so that it can be used and address later
    def load_data(self, filename: str) -> [str]:
        with open(filename, "r") as file_in:
            rows = file_in.readlines()

        return rows

    def interpret_map_data(self, rows_injec: [str] = None) -> [MapX2Y]:
        special_regex = SpecialRegexManager([r"(seeds:)(\s\d+)+", r"^([a-z\-]+)+\smap:", r"^(\d+\s){3}", r"^\n"])

        if rows_injec is None:
            assert len(self.rows) != 0
            rows = self.rows
        else:
            rows = rows_injec

        cur_map = None
        for line in rows:
            ret = special_regex.process(line)

            if ret == 0:
                # already taking care by the interpret seeds data
                pass
            elif ret == 1:
                # Create the current map
                cur_map = MapX2Y()
            elif ret == 2:
                # Read digits
                line = line.replace('\n', '')
                numbers = [int(x) for x in line.split(" ")]
                cur_map.add(numbers[0], numbers[1], numbers[2])
            elif ret == 3:
                # Close the map and register it in the lst_maps
                if cur_map is not None:
                    self.lst_maps.append(cur_map)
                    cur_map = None
            else:
                print("Should not be here")
                assert False
        else:
            # Special case : The last line of the file doesn't have an empty \n, close the last map reading
            if cur_map is not None:
                self.lst_maps.append(cur_map)

        return self.lst_maps

    def interpret_seeds_data(self, rows_injec: [str] = None) -> [int]:
        if rows_injec is None:
            assert len(self.rows) != 0
            rows = self.rows
        else:
            rows = rows_injec

        line = rows[0]
        grp_seeds_text = line.split(": ")[1].replace('\n', '').split(' ')
        self.lst_seeds = [int(seed) for seed in grp_seeds_text]
        return self.lst_seeds

    def get_next_map(self, input_data: int, layer: int) -> int:
        try:
            ret = self.get_next_map(self.lst_maps[layer].get_y(input_data), layer+1)
        except IndexError as e:
            return input_data
        else:
            return ret

    def run(self):
        for my_map in self.lst_maps:
            my_map.sort()
            my_map.normalize()

        self.lst_location = []
        for seed in self.lst_seeds:
            ret = self.get_next_map(self.lst_maps[0].get_y(seed), 1)
            self.lst_location.append(ret)

        print("Final Location List : ", end="")
        for location in self.lst_location:
            print(f"{location}, ", end="")
        print()
        print(f"min value: {min(self.lst_location)}")
