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
        print(left, right)
        sorted = sort_signal(left, right)
        print(sorted)
        #print(f"{left}, {right} have sorted value {sorted}")
        if sorted == 1:
            summed_signal += count
        count += 1

    print(f"Summed signal is {summed_signal}")


def sort_signal(left, right):
    """ sort pairs """
    # start w/ presumption that things are sorted
    # ordered = -1 is neutral, unknown state
    # change to 1 if in order, and 0 if not in order
    ordered = -1
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
            return 0
        leftcomp = left[i]
        rightcomp = right[i]
        print(leftcomp, rightcomp)
        if isinstance(leftcomp, int) and isinstance(rightcomp, int):
            if rightcomp < leftcomp:
                ordered = 0
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
        if ordered != -1:
            return ordered

    #if end of list is reached, state is unknown
    return -1


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



part1('test_signal.txt')
part1('signal.txt')