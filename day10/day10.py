day = "day10"

def main():
    part1(f"{day}/ex.txt")
    part1(f"{day}/input.txt")

    part2(f"{day}/ex.txt")
    part2(f"{day}/input.txt")

def part1(filename: str):
    print(f"Part One: {filename}")

    with open(filename, 'r') as file:
        for line in file:
            print(line)

def part2(filename: str):
    print(f"Part Two: {filename}")

    with open(filename, 'r') as file:
        for line in file:
            print(line)

if __name__ == "__main__":
    main()