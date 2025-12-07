import time

day = "day08"

def main():
    part1(f"{day}/ex.txt")
    part1(f"{day}/input.txt")

    part2(f"{day}/ex.txt")
    part2(f"{day}/input.txt")

def part1(filename: str):
    print(f"Part One: {filename}")
    start_time = time.time()
    with open(filename, 'r') as file:
        for line in file:
            print(line)
    
    print(f"Execution time: {(time.time() - start_time) * 1000} ms")

def part2(filename: str):
    print(f"Part Two: {filename}")
    start_time = time.time()
    with open(filename, 'r') as file:
        for line in file:
            print(line)

    print(f"Execution time: {(time.time() - start_time) * 1000} ms")

if __name__ == "__main__":
    main()