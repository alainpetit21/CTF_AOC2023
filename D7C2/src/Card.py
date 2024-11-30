
class Card:
    @staticmethod
    def create_from_face(c: chr) -> "Card":
        inst = Card()
        inst.face_value = c
        inst.value = Card.convert_face_to_value(c)
        return inst

    @staticmethod
    def create_from_value(v: int) -> "Card":
        inst = Card()
        inst.value = v
        return inst

    @staticmethod
    def convert_face_to_value(c: chr) -> int:
        if c == 'A':
            return 13
        elif c == 'K':
            return 12
        elif c == 'Q':
            return 11
        elif c == 'T':
            return 10
        elif c == '9':
            return 9
        elif c == '8':
            return 8
        elif c == '7':
            return 7
        elif c == '6':
            return 6
        elif c == '5':
            return 5
        elif c == '4':
            return 4
        elif c == '3':
            return 3
        elif c == '2':
            return 2
        elif c == 'J':
            return 1

    def __init__(self):
        self.face_value = ''
        self.value = -1

    def get_value(self) -> int:
        return self.value

    def __eq__(self, other: "Card") -> bool:
        if self.value == 1:
            return True

        return self.value == other.get_value()

    def __str__(self):
        return str(self.value)