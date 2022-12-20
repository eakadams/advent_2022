# code for interpreting distress signal

import json

def read_signal(signal_file):
    """read in signal"""
    with open(signal_file, 'r', encoding="utf-8") as f:
        signal_list = f.read()
    # split into pairs on newline
    signal_pairs = signal_list.split("\n\n")
    return(signal_pairs)


def sum_signal(signal_pairs):
    """take string split into pairs and send for sorting to sum"""
    summed_signal = 0
    count = 1
    for pair in signal_pairs:
        #print(pair)
        left = json.loads(pair.split("\n")[0])
        right = json.loads(pair.split("\n")[1])
        # print(left, right)
        sorted = sort_signal(left, right)
        # print(sorted)
        #print(f"{left}, {right} have sorted value {sorted}")
        if sorted == 1:
            summed_signal += count
        count += 1

    print(f"Summed signal is {summed_signal}")


def sort_signal(left, right):
    """ sort pairs """
    # start w/ presumption that things are sorted
    # ordered = 0 is neutral, unknown state
    # change to 1 if in order, and -1 if not in order
    ordered = 0
    maxlen = max(len(left), len(right))
    for i in range(maxlen):
        # first check if reached edge of either list
        if i >= len(left):
            # left ran out, ordered
            # return so don't hit empty elemtn
            return 1
        elif i >= len(right):
            # right ran out, while left still has some, not ordered
            # return value to break out, not hit empty list
            return -1
        leftcomp = left[i]
        rightcomp = right[i]
        # print(leftcomp, rightcomp)
        if isinstance(leftcomp, int) and isinstance(rightcomp, int):
            if rightcomp < leftcomp:
                ordered = -1
                # print(f"Right component is less than left")
            elif leftcomp < rightcomp:
                ordered = 1
            #if two are equal, nothing should happen, continue
        elif isinstance(leftcomp, int):
            #print('Mixed type int left')
            # right side is list
            ordered = sort_signal([leftcomp], rightcomp)
        elif isinstance(rightcomp, int):
            # print("Mixed type int right")
            # left side is list
            ordered = sort_signal(leftcomp, [rightcomp])
        else:
            # both are lists, go recursive
            ordered = sort_signal(leftcomp, rightcomp)
        # test if I am ready to return ordered status
        if ordered != 0:
            return ordered

    # if end of list is reached, state is unknown
    return 0


"""
This one kicked my butt. Looked at reddit for help.
One point was having things that were neither sorted nor unsorted
Another was switching from while to for loops and returning out of loop
I think that was the real key - breaking recursion
"""

def part1(input):
    """Part 1 of challenge"""
    signal_pairs = read_signal(input)
    sum_signal(signal_pairs)

def part2(input):
    """ Locate divider packets """
    divider1 = [[2]]
    divider2 = [[6]]
    signal_pairs = read_signal(input)
    divider1_lower_order_count = 1 # index starts at one
    divider2_lower_order_count = 2 # comes after divider 1
    for pair in signal_pairs:
        left = json.loads(pair.split("\n")[0])
        right = json.loads(pair.split("\n")[1])
        sorted_left_1 = sort_signal(left, divider1)
        sorted_right_1 = sort_signal(right, divider1)
        sorted_left_2 = sort_signal(left, divider2)
        sorted_right_2 = sort_signal(right, divider2)
        if sorted_left_1 == 1:
            #print(left)
            divider1_lower_order_count += 1
        if sorted_right_1 == 1:
            #print(right)
            divider1_lower_order_count += 1
        if sorted_left_2 == 1:
            #print(left)
            divider2_lower_order_count += 1
        if sorted_right_2 == 1:
            #print(right)
            divider2_lower_order_count += 1

    print(f"Divider {divider1} is at {divider1_lower_order_count}")
    print(f"Divider {divider2} is at {divider2_lower_order_count}")
    print(f"Decoder key is {divider1_lower_order_count * divider2_lower_order_count}")

part1('test_signal.txt')
part1('signal.txt')
part2('test_signal.txt')
part2('signal.txt')