class MapX2Y:
    def __init__(self):
        self.values: [(int, int, int)] = []

    def sort(self):
        n = len(self.values)

        for i in range(n):
            for j in range(0, n - i - 1):
                if self.values[j][0] > self.values[j+1][0]:
                    self.values[j], self.values[j+1] = self.values[j+1], self.values[j]

    def normalize(self):
        if self.values[0][0] != 0:
            self.values.insert(0,(0, 0, self.values[0][0]))
            print(f"Normalizing map at entry 0 for lenght {self.values[0][0]}")

        value = self.values[-1][0]+self.values[-1][2]
        self.values.append((value, value, 999999999999 - value))
        print(f"Normalizing map at entry {value} for lenght {999999999999-value}")

        self.values.append((999999999999, 999999999999, 0))
        print(f"Normalizing map at entry {999999999999} for lenght 0")

        my_max = len(self.values)
        for i in range(my_max-1):
            this_entry = self.values[i]
            next_entry = self.values[i+1]

            if this_entry[2]+this_entry[0] != next_entry[0]:
                new_entry_value = this_entry[2] + this_entry[0]
                new_entry_range = next_entry[0] - new_entry_value

                print(f"Normalizing map at entry {i} of value {this_entry[0]} and for length {this_entry[2]}, "
                      f"because next one is at {next_entry[0]}, thus creating a new node {i+1}, "
                      f"of values {new_entry_value}, {new_entry_value}, {new_entry_range}")
                self.values.insert(i+1, (new_entry_value, new_entry_value, new_entry_range))

    def get_y(self, val_x) -> int:
        prev_map_entry = None

        for map_entry in self.values:
            if val_x > map_entry[0]:
                prev_map_entry = map_entry
            elif val_x == map_entry[0]:
                return map_entry[1]
            else:
                offset = val_x - prev_map_entry[0]
                return prev_map_entry[1]+offset

        print("Should not be here")
        assert False
        return 0

    def get_entry(self, idx) -> (int, int, int):
        return self.values[idx]

    def add(self, dst_range_start, src_range_start, length):
        self.values.append((src_range_start, dst_range_start, length))
