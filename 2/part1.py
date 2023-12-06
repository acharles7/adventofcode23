from pathlib import Path


def find_sum(data: list[str]) -> int:
    cube_colors = {"red": 12, "green": 13, "blue": 14}
    game_sum = 0
    for line in data:
        game_name, game_sets = line.split(":")
        valid_game = True
        for game_set in game_sets.split(";"):
            for cube in game_set.split(","):
                qty, color = cube.split()
                if int(qty) > cube_colors[color]:
                    valid_game = False
                    break
            if not valid_game:
                break
        if valid_game:
            _, game_id = game_name.split()
            game_sum += int(game_id)
    return game_sum


if __name__ == '__main__':
    input_path = Path(__file__).parent / "data"
    input_data = input_path.read_text().splitlines()
    print(find_sum(input_data))
