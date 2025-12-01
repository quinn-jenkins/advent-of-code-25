day = "day01"

def main():
    # part1(f"{day}/ex.txt")    # 3
    # part1(f"{day}/input.txt") # 1168 

    # part2(f"{day}/ex.txt")  # 6
    part2(f"{day}/input.txt") # 7199

def part1(filename: str):
    print(f"Part One: {filename}")

    dialPos = 50
    exactlyZeroCount = 0
    with open(filename, 'r') as file:
        for line in file:
            dir = line[0]
            amt = int(line[1:])
            print(f"DIR: {dir} AMT: {amt}")
            if dir == "R":
                dialPos += amt
            else:
                dialPos -= amt

            dialPos = dialPos % 100
            print(f"Dial is now at: {dialPos}")

            if dialPos == 0:
                print(f"--- Dial is at exactly 0!")
                exactlyZeroCount += 1

        print(f"Dial was at zero {exactlyZeroCount} times")

def part2(filename: str):
    print(f"Part Two: {filename}")

    dialPos = 50
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            dir = line[0]
            amt = int(line[1:])
            lastDialPos = dialPos

            if amt > 100:
                # special case: some instructions turn the dial more than 1 full turn, so let's just count those and reduce the turn amt
                print(f"### AMT {amt} is greater than 100 -- doing {amt//100} full turns")
                count += amt // 100
                print(f"Count is now: {count}")
                amt = amt % 100

            if dir == "R":
                dialPos += amt
            else:
                dialPos -= amt
            print(f"START: {lastDialPos} DIR: {dir} AMT: {amt} END: {dialPos}")

            # because we counted full turns above, this will only ever pass 0 once
            # also check that we aren't starting at 0, since that would mean we've already counted this passing of 0
            if (lastDialPos != 0) and (dialPos > 100 or dialPos < 0):
                count += 1
                print(f"--- Passed zero!")
                print(f"Count is now: {count}")

            dialPos = dialPos % 100
            print(f"Dial is now at: {dialPos}")

            if dialPos == 0:
                print(f"--- Dial is at exactly 0!")
                count += 1
                print(f"Count is now: {count}")

        print(f"Dial was at zero {count} times")

if __name__ == "__main__":
    main()