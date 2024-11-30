# global array of all digits expressed as words
ar_digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


# Function to reverse a string
def reverse(string:str):
    string = "".join(reversed(string))
    return string


# Function to check for a digit expressed in words, it checks for the length of the digit word at the beginning index in
# the string passed in argument. The idea is to use this function with a spliced string. It returns a tuple of True and
# the index of the digit it founds. False and empty otherwise
def is_lettered_digit(line:str) -> (bool, str):

    idx = 1
    for word in ar_digits:
        if word == line[:len(word)]:
            return True, str(idx)

        idx += 1

    return False, ""


# Function to check for a digit expressed in words, it checks for the length of the digit word at the beginning index in
# the string passed in argument. The idea is to use this function with a spliced string. In contrast with the previous
# function, it takes a 'reverse' splices of the string and checked with the 'reverse' of the words in the array of
# digits.  It returns a tuple of True and the digit it founds. False and empty otherwise
def is_lettered_digit_reverse(line:str) -> (bool, str):

    idx = 1
    for word in ar_digits:
        if reverse(word) == line[:len(word)]:
            return True, str(idx)

        idx += 1

    return False, ""


# Function to loop through all the character in a string and first the first occurrence of a digit. The difference with
# d1c1, is that for each character, we also perform a SECOND check for digits that are expressed as words e.g 'one'.
def find_first_digit(line: str) -> str:

    idx = 0
    for letter in line:
        if letter.isdigit():
            return letter
        else:
            is_lettered, value = is_lettered_digit(line[idx:])

            if is_lettered:
                return value
        idx += 1

    return ""


# Function to loop through all the character in a REVERSED string and first the first occurrence of a digit. The
# difference with d1c1, is that for each character, we also perform a SECOND check for digits that are expressed as
# words e.g 'one'.
def find_last_digit(line: str) -> str:

    line = reverse(line)
    idx = 0
    for letter in line:
        if letter.isdigit():
            return letter
        else:
            is_lettered, value = is_lettered_digit_reverse(line[idx:])

            if is_lettered:
                return value

        idx += 1

    return ""


# Main function of the script, it will manage the main logic, and delegate special tasks to functions
def main():
    print(f'Hello World')

    # Open the file and read all lines
    with open("input.txt", "r") as inputFile:
        lines = inputFile.readlines()

        # Loop through all lines one by one
        sum_values = 0
        for line in lines:
            value_first = find_first_digit(line)
            value_last = find_last_digit(line)

            # As requested by the challenge, we concatenate those digit to a number, convert it to number and add to the
            # sum
            cal_values = value_first + value_last
            cal_values_int = int(cal_values)
            sum_values += cal_values_int

            # Print debug for each line
            print(f"Line: {line}, first: {value_first}, last: {value_last}, cal: {cal_values}, cal_int: {cal_values_int}, sum_: {sum_values}")

        # Final Print : the real sum
        print(sum_values)


if __name__ == '__main__':
    main()
