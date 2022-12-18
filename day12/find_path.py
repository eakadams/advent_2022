# code for finding path to high point
import string
import numpy as np

with open('test_heightmap.txt', 'r', encoding="utf-8") as f:
    test_height = f.read()

# read in rucksack contents
with open('heightmap.txt', 'r', encoding="utf-8") as f:
    height = f.read()

def get_topo(height):
    """Get topo from height input"""
    height_list = height.split("\n")
    topo_height = len(height_list)
    topo_width = len(height_list[0])
    topo = np.array(list(height.replace("\n", "")), 'str').reshape(topo_height, topo_width)
    return topo

def wander(height):
    """Wander topo and record lengths of successful paths"""
    topo = get_topo(height)
    # set priority / height array
    height_string = string.ascii_lowercase
    # S is at 0,0 position
    # want to just try different paths
    # how can i record branchings to explore?
    # or need to do an algorithm of some sort
    # dijkstra? or breadth-first?
    # can find examples on graph but struggle to see how to apply here
    # but can try
    # one thing I think would help me is to work backwards from end
    # since not all paths will reach, so I think that is a better way to go
    # note that I think my original thought was the equivalent of a depth-first search
    # where I wanted to explore one path to end, record, then go back to a branch
    # but i wasn't sure how to track all of that
    # may try following what is outline in this reddit comment for dijkstra:
    # https://www.reddit.com/r/adventofcode/comments/zjnruc/comment/j0240wa/?utm_source=share&utm_medium=web2x&context=3
    # decent explanation of what I want to code
    print(topo)
    shortest_path = dijkstra(topo)
    print(f"Shortest path has a distance of {shortest_path}")

def dijkstra(topo):
    """Try implementing a dijksta approach
     May be it ends up being something else
     Never done soemthing like this before
     So a fun experiment """
    node_cost = np.full(topo.shape, np.inf)
    start = np.where(topo == 'S')
    start_point = [start[0][0], start[1][0]]
    node_cost[start_point[0], start_point[1]] = 0
    # print(topo[start_point[0], start_point[1]])
    visited_nodes = np.full(topo.shape, False)
    end = np.where(topo == 'E')
    end_point = [end[0][0], end[1][0]]
    # update values of start and end point to be sure
    topo[start_point[0], start_point[1]] = 'a'
    topo[end_point[0], end_point[1]] = 'z'
    cn = start_point
    # cn = current node, array of x,y
    count = 0
    while not visited_nodes[end_point[0], end_point[1]]:
        ch = ord(topo[cn[0], cn[1]])  # current height
        # check up, down, left and right from current node
        # up first
        if (cn[1] > 0) and (ord(topo[cn[0], cn[1]-1]) <= ch+1):
            # make sure can go up, in terms of index and height
            new_cost = node_cost[cn[0], cn[1]] + 1
            if new_cost < node_cost[cn[0], cn[1]-1]:
                node_cost[cn[0], cn[1]-1] = new_cost
        # then down
        if (cn[1] < topo.shape[1]-1) and (ord(topo[cn[0], cn[1]+1]) <= ch+1):
            # make sure can go up, in terms of index and height
            new_cost = node_cost[cn[0], cn[1]] + 1
            if new_cost < node_cost[cn[0], cn[1]+1]:
                node_cost[cn[0], cn[1]+1] = new_cost
        # and left
        if (cn[0] > 0) and (ord(topo[cn[0]-1, cn[1]]) <= ch+1):
            # make sure can go up, in terms of index and height
            new_cost = node_cost[cn[0], cn[1]] + 1
            if new_cost < node_cost[cn[0]-1, cn[1]]:
                node_cost[cn[0]-1, cn[1]] = new_cost
        # finally right
        if (cn[0] < topo.shape[0]-1) and (ord(topo[cn[0]+1, cn[1]]) <= ch+1):
            # make sure can go up, in terms of index and height
            new_cost = node_cost[cn[0], cn[1]] + 1
            if new_cost < node_cost[cn[0]+1, cn[1]]:
                node_cost[cn[0]+1, cn[1]] = new_cost
        # mark current node as visited
        visited_nodes[cn[0], cn[1]] = True
        # find next node to visit
        unvisited_cost = np.ma.MaskedArray(node_cost, visited_nodes)
        #print(topo)
        #print(unvisited_cost)
        ind_min = np.unravel_index(np.ma.argmin(unvisited_cost), unvisited_cost.shape)
        cn = [ind_min[0], ind_min[1]]
        #print(unvisited_cost[cn[0], cn[1]])
        #print(topo.shape)
        if unvisited_cost[cn[0], cn[1]] > 1e9:
            print('Something has gone wrong, no nodes with cost')
            break
        count += 1
        if count > unvisited_cost.shape[0] * unvisited_cost.shape[1]:
            # should have visited all nodes, something has gone wrong
            #print(node_cost)
            break
    # get cost of path to end point
    #print(node_cost)
    #print(np.where(node_cost is np.inf))
    return node_cost[end_point[0], end_point[1]]


wander(test_height)
wander(height)

# want to get any starting point a that has the fewest steps to end point
# easiest way is to reverse path, record cost for all a points and then find lowest
# i am concerened that somehow nodes are visited and have costs assigned, even when they're not actually reachable.
# maybe I need to explicitly skip anything that has inf value and not visit

def trail(height):
    """ find trail """
    topo = get_topo(height)
    node_cost = reverse_dijkstra(topo)
    node_cost_a = np.ma.MaskedArray(node_cost, topo != 'a')
    #print(node_cost)
    #print(node_cost_a)
    print(f"Minimum number of steps for trail is {np.min(node_cost_a)}")

def reverse_dijkstra(topo):
    """Try implementing a dijksta approach
     May be it ends up being something else
     Never done soemthing like this before
     So a fun experiment """
    node_cost = np.full(topo.shape, np.inf)
    visited_nodes = np.full(topo.shape, False)
    end = np.where(topo == 'E')
    end_point = [end[0][0], end[1][0]]
    node_cost[end_point[0], end_point[1]] = 0
    # update values of start and end point to be sure
    start = np.where(topo == 'S')
    start_point = [start[0][0], start[1][0]]
    topo[start_point[0], start_point[1]] = 'a'
    topo[end_point[0], end_point[1]] = 'z'
    cn = end_point
    # cn = current node, array of x,y
    count = 0
    reachable = len(np.where(node_cost < np.inf)[0])
    while reachable > 0:
        ch = ord(topo[cn[0], cn[1]])  # current height
        #print(ch)
        # check up, down, left and right from current node
        # up first
        if (cn[1] > 0) and (ord(topo[cn[0], cn[1]-1]) >= ch-1):
            # make sure can go up, in terms of index and height
            new_cost = node_cost[cn[0], cn[1]] + 1
            if new_cost < node_cost[cn[0], cn[1]-1]:
                node_cost[cn[0], cn[1]-1] = new_cost
        # then down
        if (cn[1] < topo.shape[1]-1) and (ord(topo[cn[0], cn[1]+1]) >= ch-1):
            # make sure can go up, in terms of index and height
            new_cost = node_cost[cn[0], cn[1]] + 1
            if new_cost < node_cost[cn[0], cn[1]+1]:
                node_cost[cn[0], cn[1]+1] = new_cost
        # and left
        if (cn[0] > 0) and (ord(topo[cn[0]-1, cn[1]]) >= ch-1):
            # make sure can go up, in terms of index and height
            new_cost = node_cost[cn[0], cn[1]] + 1
            if new_cost < node_cost[cn[0]-1, cn[1]]:
                node_cost[cn[0]-1, cn[1]] = new_cost
        # finally right
        if (cn[0] < topo.shape[0]-1) and (ord(topo[cn[0]+1, cn[1]]) >= ch-1):
            # make sure can go up, in terms of index and height
            new_cost = node_cost[cn[0], cn[1]] + 1
            if new_cost < node_cost[cn[0]+1, cn[1]]:
                node_cost[cn[0]+1, cn[1]] = new_cost
        # mark current node as visited
        visited_nodes[cn[0], cn[1]] = True
        # find next node to visit
        unvisited_cost = np.ma.MaskedArray(node_cost, visited_nodes)
        #print(node_cost)
        #print(unvisited_cost)
        reachable = len(np.where(unvisited_cost < np.inf)[0]) # make sure nodes are worth exploring
        #print(topo)
        #print(unvisited_cost)
        ind_min = np.unravel_index(np.ma.argmin(unvisited_cost), unvisited_cost.shape)
        cn = [ind_min[0], ind_min[1]]
        #print(unvisited_cost[cn[0], cn[1]])
        #print(topo.shape)
        if unvisited_cost[cn[0], cn[1]] > 1e9:
            print('Something has gone wrong, no nodes with cost')
            break
        count += 1
        if count > unvisited_cost.shape[0] * unvisited_cost.shape[1]:
            # should have visited all nodes, something has gone wrong
            #print(node_cost)
            break
    # get cost of path to end point
    #print(node_cost)
    #print(np.where(node_cost is np.inf))
    return node_cost


trail(test_height)
trail(height)