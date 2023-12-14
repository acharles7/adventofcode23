from collections import defaultdict
from pathlib import Path

def find_steps(data: list[str]) -> int:
    instructions = data[0]
    maps = defaultdict(tuple)

    for d in data[2:]:
        node, dirs = d.split(" = ")
        left, right = dirs.strip()[1:-1].split(", ")
        maps[node] = (left, right)

    steps = 0
    current_node = "AAA"
    while current_node != "ZZZ":
        instruction = instructions[steps % len(instructions)]
        current_node = maps[current_node][{"L": 0, "R": 1}[instruction]]
        steps += 1
    return steps


if __name__ == '__main__':
    input_path = Path(__file__).parent / "data"
    input_data = input_path.read_text().splitlines()
    print(find_steps(input_data))  # 24253
