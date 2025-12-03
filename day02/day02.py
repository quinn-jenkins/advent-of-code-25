day = "day02"

def main():
    # part1(f"{day}/ex.txt")
    # part1(f"{day}/input.txt") # 5398419778

    # part2(f"{day}/ex.txt") 
    part2(f"{day}/input.txt")   # 15704845910

def part1(filename: str):
    print(f"Part One: {filename}")

    with open(filename, 'r') as file:
        invalidIds = []
        for idRangeStr in file.read().split(','):
            start, end = idRangeStr.split('-')
            invalidIds.extend(checkInvalid(start, end))
            print(f"start: {start} end: {end}")

        total = 0
        for invalidId in invalidIds:
            total += int(invalidId)

        print(f"Total of invalid IDs: {total}")
    
def checkInvalid(start, end, partTwo=False):
    invalidIds = []
    for id in range(int(start), int(end)+1):
        if (partTwo):
            if not isIdValidPt2(str(id)):
                invalidIds.append(id)
                print(f"- ID {id} is not valid")
        else:    
            if not isIdValid(str(id)):
                invalidIds.append(id)
                print(f"- ID {id} is not valid")
    return invalidIds

def isIdValid(idStr: str):
    idLen = len(idStr)
    # if the string has an odd length, it can't be a repeated sequence
    if idLen % 2 == 1:
        return True
    midPoint = int(idLen / 2)
    first = idStr[0:midPoint]
    second = idStr[midPoint:]
    if first == second:
        print(f"{first} == {second}")
        return False
    return True

lengthToFactors = {}

def isIdValidPt2(idStr: str):
    idLength = len(idStr)
    if idLength not in lengthToFactors:
        lengthToFactors[idLength] = factor(idLength)
    # for part 2, we need to find the factors of the length of the string, since we need to be able to split the string into x even parts
    factors = lengthToFactors[idLength]
    for fac in factors[:-1]: # ignore the last element, since that would just result in a single string
        substrings = []
        for i in range(0, idLength, fac):
            substrings.append(idStr[i:i+fac])
        print(substrings)
        first = substrings[0]
        if all(element == first for element in substrings):
            print(f"All substrings are equal -- ID is invalid")
            return False
    return True

def factor(number: int):
    factors = []
    for i in range(1, number+1):
        if number % i == 0:
            factors.append(i)
    return factors

def part2(filename: str):
    print(f"Part Two: {filename}")

    with open(filename, 'r') as file:
        invalidIds = []
        for idRangeStr in file.read().split(','):
            start, end = idRangeStr.split('-')
            invalidIds.extend(checkInvalid(start, end, True))
            print(f"start: {start} end: {end}")

        total = 0
        for invalidId in invalidIds:
            total += int(invalidId)

        print(f"Total of invalid IDs: {total}")

if __name__ == "__main__":
    main()