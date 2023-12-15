from pathlib import Path


def find_sum(data: list[str]) -> int:
    histories = [list(map(int, history.split())) for history in data]

    def diff(items: list[int]) -> list[int]:
        return [items[i+1] - items[i] for i in range(len(items)-1)]

    values = 0
    for history in histories:

        sequences = [history]
        while not all(v == 0 for v in sequences[-1]):
            sequences.append(diff(sequences[-1]))

        n = len(sequences) - 2
        prediction = 0
        while n >= 0:
            prediction = sequences[n][-1] + prediction
            n -= 1

        values += prediction

    return values


if __name__ == '__main__':
    input_path = Path(__file__).parent / "data"
    input_data = input_path.read_text().splitlines()
    print(find_sum(input_data))  # 1708206096
