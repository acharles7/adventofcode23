from pathlib import Path


str2digit = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "zero": "0"
}


def find_sum(data: list[str]) -> int:

    calibration_value_sum = 0

    for line in data:
        digit_str = ""
        l = 0
        r = len(line) - 1

        while l < len(line):
            if line[l].isdigit():
                digit_str += line[l]
                break

            if (str_digit := line[l: l+3]) in str2digit:
                digit_str += str2digit[str_digit]
                break

            if (str_digit := line[l: l+4]) in str2digit:
                digit_str += str2digit[str_digit]
                break

            if (str_digit := line[l: l+5]) in str2digit:
                digit_str += str2digit[str_digit]
                break
            l += 1

        while r >= 0:
            if line[r].isdigit():
                digit_str += line[r]
                break
            if (str_digit := line[r-2: r+1]) in str2digit:
                digit_str += str2digit[str_digit]
                break

            if (str_digit := line[r-3: r+1]) in str2digit:
                digit_str += str2digit[str_digit]
                break

            if (str_digit := line[r-4: r+1]) in str2digit:
                digit_str += str2digit[str_digit]
                break
            r -= 1

        calibration_value_sum += int(digit_str)

    return calibration_value_sum


if __name__ == '__main__':
    input_path = Path(__file__).parent / "data"
    input_data = input_path.read_text().splitlines()
    print(find_sum(input_data))
