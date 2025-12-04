day = "day04"

adjacentDirections = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def main():
    part1(f"{day}/ex.txt")
    part1(f"{day}/input.txt") # 1626

    part2(f"{day}/ex.txt")
    part2(f"{day}/input.txt") # 9173

def part1(filename: str):
    print(f"Part One: {filename}")

    with open(filename, 'r') as file:
        floor = []
        for line in file.readlines():
            floor.append(line.strip())

        dimensions = (len(floor), len(floor[0]))
        
        accessibleRolls = []
        for row in range(len(floor)):
            for col in range(len(floor[row])):
                if floor[row][col] == '@':
                    adjacents = adjacentPositions(row, col, dimensions)
                    rollCount = 0
                    for position in adjacents:
                        if floor[position[0]][position[1]] == '@':
                            rollCount += 1
                    if rollCount < 4:
                        accessibleRolls.append((row, col))
        # print(accessibleRolls)
        print(f"There are {len(accessibleRolls)} accessible rolls")           

def part2(filename: str):
    print(f"Part Two: {filename}")

    with open(filename, 'r') as file:
        floor = []
        for line in file.readlines():
            floor.append(list(line.strip()))

        dimensions = (len(floor), len(floor[0]))
        
        removedRolls = []
        removedThisPass = -1
        toRemove = []
        while not removedThisPass == 0:
            removedThisPass = 0
            for row in range(len(floor)):
                for col in range(len(floor[row])):
                    if floor[row][col] == '@':
                        adjacents = adjacentPositions(row, col, dimensions)
                        rollCount = 0
                        for position in adjacents:
                            if floor[position[0]][position[1]] == '@':
                                rollCount += 1
                        if rollCount < 4:
                            removedRolls.append((row, col))
                            toRemove.append((row, col))
                            removedThisPass += 1
            # print(f"Removed {removedThisPass} this pass.")
            for position in toRemove:
                floor[position[0]][position[1]] = '.'
            toRemove = []
        print(f"Removed {len(removedRolls)} rolls!")

# look in all 8 directions, and return any adjacent positions that are within the provided dimensions
def adjacentPositions(row: int, col: int, dimensions):
    adjacentPositions = []
    for direction in adjacentDirections:
        position = (row+direction[0], col+direction[1])
        if position[0] < dimensions[0] and position[0] >= 0 and position[1] < dimensions[1] and position[1] >= 0:
            adjacentPositions.append(position)
    return adjacentPositions 

if __name__ == "__main__":
    main()