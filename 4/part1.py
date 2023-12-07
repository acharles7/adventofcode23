from pathlib import Path


def find_points(data: list[str]) -> int:

    points = 0
    for line in data:
        expected_nums, actual_nums = line.split(":")[1].split("|")
        intersection = len(set(expected_nums.split()).intersection(set(actual_nums.split())))
        if intersection:
            points += 1 * 2 ** (intersection - 1)
    return points


if __name__ == '__main__':
    input_path = Path(__file__).parent / "data"
    input_data = input_path.read_text().splitlines()
    print(find_points(input_data))  # 26426
