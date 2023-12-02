def sum_calibration_values(file_path):
    """
    Sums the calibration values found in the document.
    Each calibration value is determined by combining the first and last digit
    in each line of the document.

    :param file_path: Path to the file containing the document.
    :return: The sum of the calibration values.
    """
    total_sum = 0

    with open(file_path, 'r') as file:
        for line in file:
            # Extract digits from the line
            digits = [char for char in line if char.isdigit()]

            if digits:
                # Form the two-digit number from the first and last digit
                # If there's only one digit, it repeats itself
                calibration_value = int(digits[0] + digits[-1])
                total_sum += calibration_value

    return total_sum

# Example usage
file_path = './day-1/input.txt'
result = sum_calibration_values(file_path)
print("Total sum of calibration values:", result)
