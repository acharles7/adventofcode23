from collections import defaultdict
from pathlib import Path
import math


def find_steps(data: list[str]) -> int:
    instructions = data[0]
    maps = defaultdict(tuple)
    for d in data[2:]:
        node, dirs = d.split(" = ")
        left, right = dirs.strip()[1:-1].split(", ")
        maps[node] = (left, right)

    a_nodes = [node for node in maps.keys() if node.endswith("A")]
    multiples = []
    for node in a_nodes:
        steps = 0
        while not node.endswith("Z"):
            instruction = instructions[steps % len(instructions)]
            node = maps[node][{"L": 0, "R": 1}[instruction]]
            steps += 1
        multiples.append(steps)
    return math.lcm(*multiples)


if __name__ == '__main__':
    input_path = Path(__file__).parent / "data"
    input_data = input_path.read_text().splitlines()
    print(find_steps(input_data))  # 12357789728873
