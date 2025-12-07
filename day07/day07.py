from functools import lru_cache
import time

day = "day07"

def main():
    part1(f"{day}/ex.txt")
    part1(f"{day}/input.txt") # 1635

    part2(f"{day}/ex.txt")
    part2(f"{day}/input.txt") # 58097428661390

def find_start(input):
    for row in range(len(input)):
        for col in range(len(input[row])):
            if input[row][col] == "S":
                return (row, col)

def part1(filename: str):
    print(f"Part One: {filename}")
    start_time = time.time()
    with open(filename, 'r') as file:
        input = [line.strip() for line in file.readlines()]
        start = find_start(input)
        beam_heads = [start]
        splitters_hit = []
        for row_num in range(start[0], len(input)-1):
            # print(f"Beam heads for row {row_num}:\n{beam_heads}")
            next_beam_heads = []
            for beam_head in beam_heads:
                if input[beam_head[0]+1][beam_head[1]] == "^":
                    beam_position = (beam_head[0]+1, beam_head[1])
                    # print(f"Hit a splitter at: {beam_position}")
                    if beam_position not in splitters_hit:
                        splitters_hit.append(beam_position)
                    if beam_head[1] > 0:
                        left_head = (beam_head[0]+1, beam_head[1]-1)
                        if left_head not in next_beam_heads:
                            next_beam_heads.append(left_head)
                    if beam_head[1] < len(input[beam_head[0]]) - 1:
                        right_head = (beam_head[0]+1, beam_head[1]+1)
                        if right_head not in next_beam_heads:
                            next_beam_heads.append(right_head)
                else:
                    # didn't hit a splitter, so just move it down
                    next_beam_heads.append((beam_head[0]+1, beam_head[1]))
            beam_heads = next_beam_heads
        print(f"Hit {len(splitters_hit)} splitters")
        print(f"Execution time: {(time.time() - start_time) * 1000} ms")

def part2(filename: str):
    print(f"Part Two: {filename}")
    start_time = time.time()
    with open(filename, 'r') as file:
        input = [line.strip() for line in file.readlines()]
        start = find_start(input)
        num_rows = len(input)
        num_cols = len(input[0])
        @lru_cache
        def move_down(row, col):
            if row < 0 or col < 0 or row >= num_rows or col >= num_cols:
                return 0 # out of bounds, not a valid move
            if row + 1 == num_rows:
                return 1 # we hit the bottom, so this is a completed "timeline"
            if input[row+1][col] == "^":
                # hit a splitter, so recursively call move down with both left and right paths
                return move_down(row+1, col+1) + move_down(row+1, col-1)
            # didn't hit a splitter, so just call move down with the next position of the beam in a straight line
            return move_down(row+1, col)

        timelines = move_down(start[0], start[1])
        print(f"Traversed {timelines} timelines")
        print(f"Execution time: {(time.time() - start_time) * 1000} ms")

if __name__ == "__main__":
    main()