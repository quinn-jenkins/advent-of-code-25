import time
import itertools
from shapely import Polygon, box
from shapely.prepared import prep

day = "day09"

def main():
    # part1(f"{day}/ex.txt")
    # part1(f"{day}/input.txt") # 4750176210

    # part2(f"{day}/ex.txt")
    part2(f"{day}/input.txt") # 1574684850

def parse_input(filename):
    with open(filename, 'r') as file:
        red_tiles = []
        input = [line.strip() for line in file.readlines()]
        for line in input:
            col, row = [int(x) for x in line.split(",")]
            red_tiles.append((row, col))
        return red_tiles
    
def connect_tiles(tile_corners):
    # create a list of line segments representing the edges (min_x, max_x, min_y, max_y)
    edges = []
    for i in range(len(tile_corners)-1):
        tile0 = tile_corners[i]
        tile1 = tile_corners[i+1]
        edges.append((min(tile0[0], tile1[0]), max(tile0[0], tile1[0]), min(tile0[1], tile1[1]), max(tile0[1], tile1[1])))
    # and also add a final edge connecting the last tile back to the first
    last = tile_corners[-1]
    first = tile_corners[0]
    edges.append((min(last[0], first[0]), max(last[0], first[0]), min(last[1], first[1]), max(last[1], first[1])))
    return edges

def is_rect_inside(edges, corner_pair):
    c1, c2 = corner_pair
    # find the min/max in each dimension
    r_min_x = min(c1[0], c2[0])
    r_max_x = max(c1[0], c2[0])
    r_min_y = min(c1[1], c2[1])
    r_max_y = max(c1[1], c2[1])
    # iterate over each of the edges, and check if any part of that line is inside the rectangle
    for edge_min_x, edge_max_x, edge_min_y, edge_max_y in edges:
        # if it overlaps vertically (crosses the horizontal line)
        if r_min_x < edge_max_x and r_max_x > edge_min_x:
            # and it overlaps horizontally (crosses the vertical line)
            if r_min_y < edge_max_y and r_max_y > edge_min_y:
                return False
    return True

def calc_area(c1, c2):
    area = (abs(c1[0] - c2[0])+1) * (abs(c1[1] - c2[1])+1)
    return area

def part1(filename: str):
    print(f"Part One: {filename}")
    start_time = time.time()
    red_tiles = parse_input(filename)
    print(red_tiles)
    tile_areas = {}
    for pair in itertools.combinations(red_tiles, 2):
        area = calc_area(pair[0], pair[1])
        tile_areas[area] = pair
    
    sorted_areas = sorted(tile_areas.keys(), reverse=True)
    print(sorted_areas)
    largest_area_pair = tile_areas[sorted_areas[0]]
    print(largest_area_pair)
    area = calc_area(largest_area_pair[0], largest_area_pair[1])
    print(sorted_areas[0])
    
    print(f"Execution time: {(time.time() - start_time) * 1000} ms")

def part2(filename: str):
    print(f"Part Two: {filename}")
    red_tiles = parse_input(filename)
    edges = connect_tiles(red_tiles)

    start_time = time.time()
    largest_area = 0
    for pair in itertools.combinations(red_tiles, 2):
        area = calc_area(pair[0], pair[1])
        # if this area is smaller, then we can skip doing boundary constraints since it won't matter
        if area <= largest_area:
            continue
        if is_rect_inside(edges, pair):
            largest_area = area

    print(f"Largest area is: {largest_area}")
    print(f"Execution time: {(time.time() - start_time) * 1000} ms")

    largest_area = 0
    start_time = time.time()
    poly = prep(Polygon(red_tiles))
    for pair in itertools.combinations(red_tiles, 2):
        area = calc_area(pair[0], pair[1])
        if area <= largest_area:
            continue
        
        c1, c2 = pair
        r_min_x = min(c1[0], c2[0])
        r_max_x = max(c1[0], c2[0])
        r_min_y = min(c1[1], c2[1])
        r_max_y = max(c1[1], c2[1])
        rect = box(r_min_x, r_min_y, r_max_x, r_max_y)
        if poly.contains(rect):
            largest_area = area
    print(f"Largest area is: {largest_area}")
    print(f"Execution time: {(time.time() - start_time) * 1000} ms")

if __name__ == "__main__":
    main()