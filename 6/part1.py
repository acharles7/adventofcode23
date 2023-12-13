from pathlib import Path


def find_ways(data: list[str]) -> int:

    race_time = list(map(int, data[0].split(":")[1].strip().split()))
    race_dist = list(map(int, data[1].split(":")[1].strip().split()))
    ways = 1

    for rt, rd in zip(race_time, race_dist):
        ways *= sum(1 for ht in range(rt + 1) if (rt - ht) * ht > rd)
    return ways


if __name__ == '__main__':
    input_path = Path(__file__).parent / "data"
    input_data = input_path.read_text().splitlines()
    print(find_ways(input_data))  # 393120
