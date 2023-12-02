## GPT4 has problems with this script, it will not calculate the correct result, I still keep it here for inspiration

def sum_calibration_values(file_path):
    string_numbers = {
        "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }

    total_sum = 0

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            num_list = []

            i = 0
            while i < len(line):
                # Check if the character is a digit
                if line[i].isdigit():
                    num_list.append(line[i])
                    i += 1
                else:
                    # Check for spelled-out numbers
                    for word, digit in string_numbers.items():
                        if line.startswith(word, i):
                            num_list.append(digit)
                            i += len(word)  # Skip past the spelled-out number
                            break
                    else:
                        i += 1  # Increment if no match is found

            # Calculate and add the calibration value
            if num_list:
                calibration_value = int(num_list[0] + num_list[-1])
                total_sum += calibration_value

    return total_sum

# Path to the input file
file_path = './day-1/input.txt'

# Calculate the sum
result = sum_calibration_values(file_path)
print("Total sum of calibration values:", result)
