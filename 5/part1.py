from pathlib import Path


def find_location(data: list[str]) -> int:

    seeds = []
    seed_to_soil = []
    soil_to_fertilizer = []
    fertilizer_to_water = []
    water_to_light = []
    light_to_temperature = []
    temperature_to_humidity = []
    humidity_to_location = []

    sequence = [
        ("seed_to_soil", seed_to_soil),
        ("soil_to_fertilizer", soil_to_fertilizer),
        ("fertilizer_to_water", fertilizer_to_water),
        ("water_to_light", water_to_light),
        ("light_to_temperature", light_to_temperature),
        ("temperature_to_humidity", temperature_to_humidity),
        ("humidity_to_location", humidity_to_location)
    ]

    def build_maps():
        n = 0
        while n < len(data):
            line = data[n]
            if not line:
                n += 1
                continue
            match line.split(":"):
                case ["seeds", input_seeds]:
                    seeds.extend(map(int, input_seeds.split()))
                    n += 1
                case ["seed-to-soil map", _]:
                    n += 1
                    while data[n]:
                        seed_to_soil.append(tuple(map(int, data[n].split())))
                        n += 1
                case ["soil-to-fertilizer map", _]:
                    n += 1
                    while data[n]:
                        soil_to_fertilizer.append(tuple(map(int, data[n].split())))
                        n += 1
                case ["fertilizer-to-water map", _]:
                    n += 1
                    while data[n]:
                        fertilizer_to_water.append(tuple(map(int, data[n].split())))
                        n += 1
                case ["water-to-light map", _]:
                    n += 1
                    while data[n]:
                        water_to_light.append(tuple(map(int, data[n].split())))
                        n += 1
                case ["light-to-temperature map", _]:
                    n += 1
                    while data[n]:
                        light_to_temperature.append(tuple(map(int, data[n].split())))
                        n += 1
                case ["temperature-to-humidity map", _]:
                    n += 1
                    while data[n]:
                        temperature_to_humidity.append(tuple(map(int, data[n].split())))
                        n += 1
                case ["humidity-to-location map", _]:
                    n += 1
                    while n < len(data) and data[n]:
                        humidity_to_location.append(tuple(map(int, data[n].split())))
                        n += 1

    build_maps()
    lowest_location = float('inf')
    for seed in seeds:
        next_lookup = seed
        for name, entity_map in sequence:
            for d, s, r in entity_map:
                if next_lookup in range(s, s+r):
                    next_lookup = d + next_lookup - s
                    break
        lowest_location = min(lowest_location, next_lookup)
    return lowest_location


if __name__ == '__main__':
    input_path = Path(__file__).parent / "data"
    input_data = input_path.read_text().splitlines()
    print(find_location(input_data))  # 424490994
