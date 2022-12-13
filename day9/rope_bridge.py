# code for understanding rope bridge
import math

with open('test_moves.txt', 'r', encoding="utf-8") as f:
    test_moves = f.read()

with open('test2_moves.txt', 'r', encoding="utf-8") as f:
    test2_moves = f.read()

# read in rucksack contents
with open('moves.txt', 'r', encoding="utf-8") as f:
    moves = f.read()

move_list = moves.split("\n")
test_move_list = test_moves.split("\n")
test2_move_list = test2_moves.split("\n")

def get_locs(move_list):
    """Get locations given move list"""
    head_loc_list = [(0,0)]
    tail_loc_list = [(0,0)]
    for move in move_list:
        dir = move.split(" ")[0]
        steps = int(move.split(" ")[1])
        for step in range(steps):
            current_head_loc = head_loc_list[-1]
            if dir == 'U':
                new_head_loc = (current_head_loc[0], current_head_loc[1]+1)
            if dir == 'D':
                new_head_loc = (current_head_loc[0], current_head_loc[1] - 1)
            if dir == 'R':
                new_head_loc = (current_head_loc[0] + 1, current_head_loc[1])
            if dir == 'L':
                new_head_loc = (current_head_loc[0] - 1, current_head_loc[1])
            # append new head loc
            head_loc_list.append(new_head_loc)
            # test if tail needs to move
            current_tail_loc = tail_loc_list[-1]
            dist_head_tail = ((new_head_loc[0] - current_tail_loc[0])**2 +
                              (new_head_loc[1] - current_tail_loc[1])**2)**(1/2)
            offset_x = new_head_loc[0] - current_tail_loc[0]
            offset_y = new_head_loc[1] - current_tail_loc[1]
            if dist_head_tail > 1.5:
                # need to move tail
                # have to test if moving just one step or diagonally
                # always move one step in direction of head
                if abs(offset_x) > 0 and abs(offset_y) > 0:
                    new_tail_loc = (current_tail_loc[0] + math.copysign(1, offset_x),
                                    current_tail_loc[1] + math.copysign(1, offset_y))
                else:
                    if dir == 'U':
                        new_tail_loc = (current_tail_loc[0], current_tail_loc[1] + 1)
                    if dir == 'D':
                        new_tail_loc = (current_tail_loc[0], current_tail_loc[1] - 1)
                    if dir == 'R':
                        new_tail_loc = (current_tail_loc[0] + 1, current_tail_loc[1])
                    if dir == 'L':
                        new_tail_loc = (current_tail_loc[0] - 1, current_tail_loc[1])
                # append new tail loc
                tail_loc_list.append(new_tail_loc)
    set_tails = set(tail_loc_list)
    print(f"There are {len(set_tails)} unique tail locations")


get_locs(test_move_list)
get_locs(move_list)

def follow_rope(move_list):
    """Follow the tail of a rope of length 10"""
    rope_list = [[(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)],
                 [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)]]
    for move in move_list:
        dir = move.split(" ")[0]
        steps = int(move.split(" ")[1])
        for _ in range(steps):
            # first, head moves
            head_loc = rope_list[0][-1]
            new_head_loc = do_head_move(dir, head_loc)
            rope_list[0].append(new_head_loc)
            # then go through tail knots
            for i in range(1,len(rope_list)):
                tail_loc = rope_list[i][-1]
                rel_head_loc = rope_list[i-1][-1]
                dist_head_tail = ((rel_head_loc[0] - tail_loc[0]) ** 2 +
                                  (rel_head_loc[1] - tail_loc[1]) ** 2) ** (1 / 2)
                if dist_head_tail > 1.5:
                    new_tail_loc = do_tail_move(dir, rel_head_loc, tail_loc)
                    rope_list[i].append(new_tail_loc)
        #print(move, rope_list[0][-1])
        #print(move, rope_list[-2][-1])
        #print(move, rope_list[-1][-1])
    set_tail_locs = set(rope_list[-1])
    print(f"There are {len(set_tail_locs)} unique tail locations")
    print(f"There are {len(rope_list[-1])} total tail locations")


def do_head_move(dir, current_head_loc):
    """Return a new head loc"""
    if dir == 'U':
        new_head_loc = (current_head_loc[0], current_head_loc[1] + 1)
    if dir == 'D':
        new_head_loc = (current_head_loc[0], current_head_loc[1] - 1)
    if dir == 'R':
        new_head_loc = (current_head_loc[0] + 1, current_head_loc[1])
    if dir == 'L':
        new_head_loc = (current_head_loc[0] - 1, current_head_loc[1])
    return new_head_loc


def do_tail_move(dir, head_loc, tail_loc):
    """Move the tail"""
    offset_x = head_loc[0] - tail_loc[0]
    offset_y = head_loc[1] - tail_loc[1]
    # check for diagonal
    if abs(offset_x) > 0 and abs(offset_y) > 0:
        new_tail_loc = (tail_loc[0] + math.copysign(1, offset_x),
                        tail_loc[1] + math.copysign(1, offset_y))
    else:
        # move in direction of local head
        # find which way offset exists
        if abs(offset_x) > 0:
            new_tail_loc = (tail_loc[0] + math.copysign(1, offset_x),
                            tail_loc[1])
        else:
            new_tail_loc = (tail_loc[0],
                            tail_loc[1] + math.copysign(1, offset_y))
    return new_tail_loc


follow_rope(test_move_list)
follow_rope(test2_move_list)
follow_rope(move_list)