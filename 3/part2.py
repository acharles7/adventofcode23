from collections import defaultdict
from pathlib import Path


def find_ratio(data: list[str]) -> int:

    grid = [list(line) for line in data]
    n, m = len(grid), len(grid[0])
    gears = defaultdict(list)
    gear_ratio = 0

    def nearby_stars(start: tuple[int, int], end: tuple[int, int]) -> tuple[int, int]:
        p1, q1 = start
        p2, q2 = end

        # top row
        top_row = grid[x := max(0, p1-1)][(y := max(0, q1-1)): min(q2+1, m)]
        for idx, item in enumerate(top_row, start=y):
            if item == "*":
                return x, idx
        # bottom row
        bottom_row = grid[x := min(m-1, p1+1)][(y := max(0, q1-1)): min(q2+1, m)]
        for idx, item in enumerate(bottom_row, start=y):
            if item == "*":
                return x, idx
        # sides
        left = grid[p1][y := max(0, q1-1)]
        if left == "*":
            return p1, y

        right = grid[p1][y := min(n-1, q2)]
        if right == "*":
            return p1, y

    for i in range(len(grid)):
        j = 0
        while j < n:
            char = grid[i][j]
            if not char.isdigit():
                j += 1
                continue
            start = (i, j)
            num = ""
            while j < n:
                if not grid[i][j].isdigit():
                    break
                num += grid[i][j]
                j += 1
            end = (i, j)
            if star := nearby_stars(start, end):
                gears[star].append(int(num))

    for star, nums in gears.items():
        if len(nums) >= 2:
            ratio = 1
            for num in nums:
                ratio *= num
            gear_ratio += ratio

    return gear_ratio



if __name__ == '__main__':
    input_path = Path(__file__).parent / "data"
    input_data = input_path.read_text().splitlines()
    print(find_ratio(input_data))  # 81166799
