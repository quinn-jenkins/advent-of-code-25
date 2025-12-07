from math import prod

day = "day06"

def main():
    part1(f"{day}/ex.txt")
    part1(f"{day}/input.txt") # 7098065460541

    part2(f"{day}/ex.txt")
    part2(f"{day}/input.txt") # 13807151830618

def part1(filename: str):
    print(f"Part One: {filename}")

    with open(filename, 'r') as file:
        input = [line.strip().split() for line in file]
        rotated = list(zip(*input[::-1]))
        total = 0
        for line in rotated:
            op = line[0]
            if op == "*":
                count = 1
                for val in line[1:]:
                    count *= int(val)
                total += count
            elif op == "+":
                count = 0
                for val in line[1:]:
                    count += int(val)
                total += count
        print (f"P1 total: {total}")

def eval_current_vals(op: str, vals) -> int:
    if len(vals) == 0:
        return 0
    if op == "+":
        return sum(vals)
    elif op == "*":
        return prod(vals)

def part2(filename: str):
    print(f"Part Two: {filename}")

    with open(filename, 'r') as file:
        input = [line.removesuffix('\n') for line in file.readlines()]
        ops = input[-1]
        vals = input[:-1]

        currOp = ops[0]
        currVals = []
        total = 0
        # iterate over the bottom line that contains the operators
        # assumption is that the operator is in the first column of a new group of numbers
        # when we find a new operator symbol in that row, evaluate the previous grouping of numbers and reset
        # look through the rest of the input in the same column and collect any numbers in a string, and at the end convert that string to an integer, add to current number group
        for col in range(len(ops)):
            if ops[col] == "+" or ops[col] == "*":
                total += eval_current_vals(currOp, currVals)
                currVals = []
                currOp = ops[col]

            digits = []
            for row in vals:
                if row[col] != " ":
                    val = row[col]
                    digits.append(val)
            if len(digits) != 0:
                newVal = int("".join(map(str, digits)))
                currVals.append(newVal)
        # evaluate the last group of numbers
        total += eval_current_vals(currOp, currVals)
        print(f"P2 total: {total}")

if __name__ == "__main__":
    main()