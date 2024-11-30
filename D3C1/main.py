SYMBOLS = "%*#&$@/=+-"
processing_queue = set()
data = []


# This function will only load the data as 2D array and return it so that it can be used and address later
def load_data(filename: str) -> [[chr]]:
    with open(filename, "r") as file_in:
        rows = file_in.readlines()

    return rows


# This function will act as generator to yield, one at a time, the next symbol found
def symbols_scanner() -> (int, int):

    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] in SYMBOLS:
                yield x, y


# This function will act as generator to yield, one at a time, number found around the found symbol
def kernel_processor(x: int, y: int) -> (int, int):
    max_y = len(data)
    max_x = len(data[0])

    for j in range(max(0, y - 1), min(max_y, y + 2)):
        for i in range(max(0, x - 1), min(max_x, x + 2)):
            value = "".join(data[j][i])
            if value.isdigit():
                yield i, j


# This function will return the whole number found at x & y, scanning back and forth and return the value + it starting
# coordinate as a tuple of value and tuple of startX and startY.
def detect_whole_number(x: int, y: int) -> (int, (int, int)):
    max_x = len(data[0])

    # Detect left for the beginning of the number, and record the starting point
    lst_number = []
    start = [-1, y]
    for i in range(x, 0-1, -1):
        value = "".join(data[y][i])
        if value.isdigit():
            lst_number.insert(0, data[y][i])
            start[0] = i
        else:
            break

    # Detect right for the end of the number
    for i in range(x+1, max_x-1, 1):
        value = "".join(data[y][i])
        if value.isdigit():
            lst_number.append(data[y][i])
        else:
            break

    strnum = "".join(lst_number)
    retval = int(strnum)
    return retval, (start[0], start[1])


# When a new number is found, it is added to a set (uniqued list) that will act as a queue for later processing
def add_number_to_processing_queue(x: int, y: int):
    processing_queue.add((x, y))


def process_queue() -> int:

    sum_num = 0
    for coordinate in processing_queue:
        number, coordinate = detect_whole_number(coordinate[0], coordinate[1])
        sum_num += number

    return sum_num


def main():
    global data
    print(f'Hi, d3c1')

    # data = load_data("example.txt")
    data = load_data("input.txt")

    for coord_symbol in symbols_scanner():
        for coord_digit in kernel_processor(coord_symbol[0], coord_symbol[1]):
            number, coord_start_numb = detect_whole_number(coord_digit[0], coord_digit[1])

            add_number_to_processing_queue(coord_start_numb[0], coord_start_numb[1])

    sum_value = process_queue()
    print(sum_value)


if __name__ == '__main__':
    main()
