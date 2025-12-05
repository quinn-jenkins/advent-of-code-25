day = "day05"

def main():
    # part1(f"{day}/ex.txt")
    # part1(f"{day}/input.txt") # 511

    # part2(f"{day}/ex.txt")
    part2(f"{day}/input.txt") # 350939902751909

def part1(filename: str):
    print(f"Part One: {filename}")

    with open(filename, 'r') as file:
        freshIngredients = []
        availableIngredients = []
        fresh = True
        for line in file.read().splitlines():
            if line == "":
                fresh = False
                continue
            if fresh:
                start, end = [int(x) for x in line.split("-")]
                freshIngredients.append((start, end))
            else:
                availableIngredients.append(int(line))

        freshIngredients.sort()
        availableIngredients.sort()

        print(f"Fresh: {freshIngredients}")
        print(f"Available: {availableIngredients}")

        count = 0
        for ingr in availableIngredients:
            for freshRange in freshIngredients:
                if ingr in range(freshRange[0], freshRange[1]+1):
                    count += 1
                    print(f"{ingr} is fresh")
                    break
        print(f"There are {count} fresh ingredients")

            

def part2(filename: str):
    print(f"Part Two: {filename}")

    with open(filename, 'r') as file:
        freshIngredients = []
        for line in file.read().splitlines():
            if line == "":
                break

            start, end = [int(x) for x in line.split("-")]
            freshIngredients.append((start, end))

        freshIngredients.sort()
        mergedRanges = [freshIngredients[0]]
        for start, end in freshIngredients[1:]:
            # if the previous range contains the start of this range, we can merge it
            if mergedRanges[-1][1] >= start:
                # replace the previous range with a new range that goes from the original start to whichever is the furthest end
                mergedRanges[-1] = (mergedRanges[-1][0], max(mergedRanges[-1][1], end))
            else:
                mergedRanges.append((start, end))

        count = 0
        for ingrRange in mergedRanges:
            count += ingrRange[1] - ingrRange[0] + 1 # account for ranges being inclusive

        print(f"total fresh ingredients: {count}")




if __name__ == "__main__":
    main()