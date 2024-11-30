import re


class SpecialRegexManager:
    def __init__(self, lst_pattern: [str]):
        self.lst_pattern = lst_pattern

    def process(self, data: str):

        i = 0
        for pat in self.lst_pattern:
            match = re.match(pat, data)

            if match:
                return i

            else:
                i += 1
