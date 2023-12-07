from collections import defaultdict
from pathlib import Path


def find_points(data: list[str]) -> int:
    card_counter = defaultdict(int)

    for line in data:
        card, numbers = line.split(":")
        card_id = int(card.split()[1])
        card_counter[card_id] += 1

        expected_numbers, actual_numbers = numbers.split("|")
        expected_numbers, actual_numbers = set(expected_numbers.split()), set(actual_numbers.split())
        intersection = len(actual_numbers.intersection(expected_numbers))
        if intersection:
            for _ in range(card_counter[card_id]):
                for next_card in range(intersection):
                    card_counter[card_id+next_card+1] += 1

    points = sum(card_counter.values())
    return points


if __name__ == '__main__':
    input_path = Path(__file__).parent / "data"
    input_data = input_path.read_text().splitlines()
    print(find_points(input_data))  # 6227972
