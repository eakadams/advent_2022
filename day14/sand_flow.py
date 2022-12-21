# code for looking at sand flow in cave

import numpy as np


def parse_input(rock_file):
    """ read rock input """
    with open(rock_file, 'r', encoding="utf-8") as f:
        rock_lines = f.readlines()
    return rock_lines


def get_rock_structure(rock_lines):
    """ get numpy array that has rock structure """
    rock_list = []
    # min and max values come from 500, 0
    # origin point of sand
    # would be more flexible to have this as input
    max_x = 500
    min_x = 500
    max_y = 0
    min_y = 0
    for rock in rock_lines:
        rock_nodes = rock.split("->")
        node_list = []
        for node in rock_nodes:
            int_node = [int(n) for n in node.strip().split(',')]
            node_list.append(int_node)
            # also test min / max and update
            x = int(node.strip().split(',')[0])
            y = int(node.strip().split(',')[1])
            if x > max_x:
                max_x = x
            if x < min_x:
                min_x = x
            if y > max_y:
                max_y = y
            if y < min_y:
                min_y = y
        rock_list.append(node_list)
    print(min_x, max_x, min_y, max_y)
    return rock_list


def visualize_rock_structure(rock_array):
    """ take rock array and visualize """
    pass


def part1(rock_file):
    """ Do part1, start with exploration """
    rock_lines = parse_input(rock_file)
    rock_list = get_rock_structure(rock_lines)
    print(rock_list)


part1('test_rocks.txt')
