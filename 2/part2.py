from pathlib import Path


def find_sum(data: list[str]) -> int:
    cube_power_sum = 0
    for line in data:
        game_id, game_sets = line.split(":")
        cube_colors = {"red": 0, "green": 0, "blue": 0}
        cube_power = 1
        for game_set in game_sets.split(";"):
            for cube in game_set.split(","):
                qty, color = cube.split()
                cube_colors[color] = max(int(qty), cube_colors[color])
        for num in cube_colors.values():
            cube_power *= num
        cube_power_sum += cube_power
    return cube_power_sum


if __name__ == '__main__':
    input_path = Path(__file__).parent / "data"
    input_data = input_path.read_text().splitlines()
    print(find_sum(input_data))