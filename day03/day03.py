day = "day03"

def main():
    # part1(f"{day}/ex.txt")
    # part1(f"{day}/input.txt") # 17766

    # part2(f"{day}/ex.txt")
    part2(f"{day}/input.txt") # 176582889354075

    # 176582889354038 too low

def part1(filename: str):
    print(f"Part One: {filename}")

    with open(filename, 'r') as file:
        totalJoltage = 0
        for line in file.readlines():
            line = line.strip()
            print(line)
            # find the first occurrence of the highest value in the line (can break if you find a 9, and stop 1 index from the end because you need a 2nd digit)
            # find the highest value to the right of the first index
            firstBattery = 0
            secondBattery = 0
            for char in line[:-1]:
                value = int(char)
                if value > firstBattery:
                    firstBattery = value
                    secondBattery = 0
                elif value > secondBattery:
                    secondBattery = value
            if secondBattery == 0 or int(line[-1]) > secondBattery:
                secondBattery = int(line[-1])

            joltage = 10 * firstBattery + secondBattery
            print(f"Largest Joltage is: {joltage}")
            totalJoltage += joltage
        print(f"Total Joltage is: {totalJoltage}")

def part2(filename: str):
    print(f"Part Two: {filename}")

    with open(filename, 'r') as file:
        totalJoltage = 0
        for line in file:
            line = [int(char) for char in line.strip()]
            print(line)
            batteries = line[:12]
            print(batteries)
            for potentialReplacement in line[12:]:
                # we know we should replace a battery, but we need to know which one to replace
                # look at each battery left to right -- if the battery at index i < i+1, then removing the battery at index i would increase the joltage
                for i in range(12):
                    # special case -- check if we should replace the last battery in the list
                    if i == 11 and potentialReplacement > batteries[11]:
                        removed = batteries.pop(11)
                        batteries.append(potentialReplacement)
                        print(f"Removing battery {removed} and adding {potentialReplacement}")
                        print(batteries)
                        break
                    # look to the right (if possible) and remove the battery at i if the battery at i+1 is larger
                    elif i < 11 and batteries[i] < batteries[i+1]:
                        removed = batteries.pop(i)
                        batteries.append(potentialReplacement)
                        print(f"Removing battery {removed} and adding {potentialReplacement}")
                        print(batteries)
                        break
            highestJoltage = int(''.join(map(str, batteries)))
            print(f"Highest Joltage: {highestJoltage}")
            totalJoltage += highestJoltage
        print(f"Total Joltage: {totalJoltage}")

if __name__ == "__main__":
    main()