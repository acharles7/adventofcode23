from pathlib import Path


def find_sum(data: list[str]) -> int:

    calibration_value_sum = 0
    for line in data:
        digit_str = ""
        for char in line:
            if char.isdigit():
                digit_str += char
                break
        for char in line[::-1]:
            if char.isdigit():
                digit_str += char
                break
        calibration_value_sum += int(digit_str)

    return calibration_value_sum


if __name__ == '__main__':
    input_path = Path(__file__).parent / "data"
    input_data = input_path.read_text().splitlines()
    print(find_sum(input_data))
