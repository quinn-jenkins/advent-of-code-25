import time
import itertools
import math
from math import prod

day = "day08"

def main():
    # part1(f"{day}/ex.txt")
    # part1(f"{day}/input.txt") # 68112

    # part2(f"{day}/ex.txt")
    part2(f"{day}/input.txt") # 44543856

def part1(filename: str):
    print(f"Part One: {filename}")
    start_time = time.time()
    circuits = []
    distance_node_pairs = {}
    nodes = []
    with open(filename, 'r') as file:
        input = [line.strip() for line in file.readlines()]
        for line in input:
            x, y, z = [int(val) for val in line.split(",")]
            nodes.append((x, y, z))
    for node_pair in itertools.combinations(nodes, 2):
        distance = math.dist(node_pair[0], node_pair[1])
        distance_node_pairs[distance] = node_pair
    sorted_distances = sorted(distance_node_pairs.keys())
    num_iters = 10 if "ex" in filename else 1000
    print(f"Number of iterations: {num_iters}")
    for i in range(num_iters):
        d = sorted_distances[i]
        node_pair = distance_node_pairs[d]
        node0_circuit = None
        node1_circuit = None
        for circuit in circuits:
            if node_pair[0] == circuit or node_pair[0] in circuit:
                node0_circuit = circuit
            if node_pair[1] == circuit or node_pair[1] in circuit:
                node1_circuit = circuit
        if node0_circuit is None and node1_circuit is None:
            # neither belongs to a circuit, so make a new one
            circuits.append(set([node_pair[0], node_pair[1]]))
        elif node0_circuit is not None and node1_circuit is not None:
            if node0_circuit == node1_circuit:
                # these 2 already belong to the same circuit, so skip
                continue
            # combine the 2 circuits
            circuits.remove(node0_circuit)
            circuits.remove(node1_circuit)
            circuits.append(node0_circuit.union(node1_circuit))
        else:
            # add whichever the "free" node is to the existing circuit
            if node0_circuit is not None:
                node0_circuit.add(node_pair[1])
            else:
                node1_circuit.add(node_pair[0])
        
    sorted_circuits = sorted(circuits, key=len, reverse=True)
    product=1
    for i in range(3):
        print(f"Circuit {i} length {len(sorted_circuits[i])}")
        product *= len(sorted_circuits[i])

    print(f"Solution: {product}")
    print(f"Execution time: {(time.time() - start_time) * 1000} ms")

def part2(filename: str):
    print(f"Part Two: {filename}")
    start_time = time.time()

    nodes = []
    circuits = []
    distance_node_pairs = {}
    with open(filename, 'r') as file:
        input = [line.strip() for line in file.readlines()]
        for line in input:
            x, y, z = [int(val) for val in line.split(",")]
            # to start, each node is its own circuit
            nodes.append((x, y, z))
        
        for node_pair in itertools.combinations(nodes, 2):
            distance = math.dist(node_pair[0], node_pair[1])
            distance_node_pairs[distance] = node_pair
        sorted_distances = sorted(distance_node_pairs.keys())

        for node in nodes:
            circuits.append(set([node]))

        # keep going until we only have 1 circuit left
        last_connected = None
        for distance in sorted_distances:
            # keep going until we've connected all nodes into a single circuit
            if len(circuits) == 1:
                print(f"Last connected nodes: {last_connected}")
                print(f"Solution: {last_connected[0][0] * last_connected[1][0]}")
                break
            # get the next closest pair of nodes
            node_pair = distance_node_pairs[distance]
            c0 = None
            c1 = None
            # find which circuit each node in the pair belongs to
            for c in circuits:
                if node_pair[0] in c:
                    c0 = c
                if node_pair[1] in c:
                    c1 = c
            # remove each existing circuit (although only remove it once if they're the same)
            circuits.remove(c0)
            if c0 != c1:
                circuits.remove(c1)
            # and replace it with the union of those circuits
            circuits.append(c0.union(c1))
            last_connected = node_pair
            


    
    print(f"Execution time: {(time.time() - start_time) * 1000} ms")

if __name__ == "__main__":
    main()