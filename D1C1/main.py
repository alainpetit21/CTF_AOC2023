# Function to loop through all the character in a string and first the first occurrence of a digit
def find_first_digit(line: str) -> str:
    for letter in line:
        if letter.isdigit():
            return letter

    return ""


# Function to loop through all the character in a REVERSED string and first the first occurrence of a digit
def find_last_digit(line: str) -> str:
    for letter in reversed(line):
        if letter.isdigit():
            return letter

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
