from pathlib import Path


def find_sum(data: list[str]) -> int:

    grid = [list(line) for line in data]
    n, m = len(grid), len(grid[0])

    def nearby_symbol(start: tuple[int, int], end: tuple[int, int]) -> bool:
        p1, q1 = start
        p2, q2 = end

        top_row = grid[max(0, p1-1)][max(0, q1-1): min(q2+1, m)]
        bottom_row = grid[min(m-1, p1+1)][max(0, q1-1): min(q2+1, m)]
        left = grid[p1][max(0, q1-1)]
        right = grid[p1][min(n-1, q2)]

        neighbors = top_row + bottom_row + [left, right]
        for neighbor in neighbors:
            if neighbor.isdigit() or neighbor == ".":
                continue
            else:
                return True
        return False

    parts_sum = 0
    for i in range(len(grid)):
        j = 0
        while j < n:
            char = grid[i][j]
            if not char.isdigit():
                j += 1
                continue
            start = i, j
            num = ""
            while j < n:
                if not grid[i][j].isdigit():
                    break
                num += grid[i][j]
                j += 1
            end = i, j
            if nearby_symbol(start, end):
                parts_sum += int(num)
    return parts_sum


if __name__ == '__main__':
    input_path = Path(__file__).parent / "data"
    input_data = input_path.read_text().splitlines()
    print(find_sum(input_data))  # 549908
