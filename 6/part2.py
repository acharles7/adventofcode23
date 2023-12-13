from pathlib import Path


def find_ways(data: list[str]) -> int:

    race_time = int("".join(data[0].split(":")[1].strip().split()))
    race_dist = int("".join(data[1].split(":")[1].strip().split()))

    return sum(1 for ht in range(race_time + 1) if (race_time - ht) * ht > race_dist)


if __name__ == '__main__':
    input_path = Path(__file__).parent / "data"
    input_data = input_path.read_text().splitlines()
    print(find_ways(input_data))  # 36872656
