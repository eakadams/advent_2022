# code for exploring trees
import numpy as np

with open('test_trees.txt', 'r', encoding="utf-8") as f:
    test_trees = f.read()

# read in rucksack contents
with open('trees.txt', 'r', encoding="utf-8") as f:
    trees = f.read()

def get_forest(trees):
    """Get forest array from trees input"""
    tree_list = trees.split("\n")
    forest_height = len(tree_list)
    forest_width = len(tree_list[0])
    forest = np.array(list(trees.replace("\n", "")), 'uint8').reshape(forest_height, forest_width)
    return forest

def find_visible_trees(forest):
    """Find how many trees are visible"""
    n_vis = 0
    # first and last row are fully visible
    n_rows = len(forest)
    n_columns = len(forest[0])
    n_vis += 2 * n_columns
    # first and last column are fully visible, but already counted rows
    n_vis += 2 * n_rows - 4
    # now iterate over remaining trees
    for row in range(1,n_rows-1):
        for col in range(1, n_columns -1):
            tree_height = forest[row, col]
            # tree visible from above?
            above = forest[:,col][0:row]
            if tree_height > np.amax(above):
                n_vis += 1
                # print(f"Tree height {tree_height} at location {row}, {col} is visible from above")
                continue
            down = forest[:,col][row+1:]
            if tree_height > np.amax(down):
                n_vis += 1
                # print(f"Tree height {tree_height} at location {row}, {col} is visible from below")
                continue
            left = forest[row,:][:col]
            if tree_height > np.amax(left):
                n_vis += 1
                # print(f"Tree height {tree_height} at location {row}, {col} is visible from the left")
                continue
            right = forest[row,:][col+1:]
            if tree_height > np.amax(right):
                n_vis += 1
                # print(f"Tree height {tree_height} at location {row}, {col} is visible from the right")
                continue
    return n_vis

def get_scenic_score(forest):
    """Take forest as np array and get scenic score"""
    n_rows = len(forest)
    n_columns = len(forest[0])
    scenic_score = np.full((n_rows, n_columns),0)
    for row in range(n_rows):
        for col in range(n_columns):
            tree_height = forest[row,col]
            # get score for view up the colum
            if row == 0:
                up_score = 0
            else:
                trees_up = forest[:row,col]
                ind_block = np.where(trees_up >= tree_height)[0]
                if len(ind_block) == 0:
                    # not blocked, length of view
                    up_score = len(trees_up)
                else:
                    up_score = np.min(np.abs(ind_block - row))
            # print(up_score)
            # get score for the view down the column
            if row == (n_rows - 1):
                # last row
                down_score = 0
            else:
                trees_down = forest[row+1:,col]
                ind_block = np.where(trees_down >= tree_height)[0]
                if len(ind_block) == 0:
                    down_score = len(trees_down)
                else:
                    down_score = np.min(ind_block) + 1
            # get view to left
            if col == 0:
                left_score = 0
            else:
                left_trees = forest[row,:col]
                ind_block = np.where(left_trees >= tree_height)[0]
                if len(ind_block) == 0:
                    left_score = len(left_trees)
                else:
                    left_score = np.min(np.abs(ind_block - col))
            # get view to right
            if col == (n_columns - 1):
                right_score = 0 # edge of forest
            else:
                trees_right = forest[row,col+1:]
                ind_block = np.where(trees_right >= tree_height)[0]
                if len(ind_block) == 0:
                    right_score = len(trees_right)
                else:
                    right_score = np.min(ind_block) + 1
            score = up_score * down_score * left_score * right_score
            scenic_score[row,col] = score

    print(f"Max scenic score is {np.amax(scenic_score)}")


test_forest = get_forest(test_trees)
print(test_forest)

forest = get_forest(trees)

test_vis = find_visible_trees(test_forest)
print(f"There are {test_vis} trees visible in test forest")

vis = find_visible_trees(forest)
print(f"There are {vis} trees visible in test forest")

get_scenic_score(test_forest)
get_scenic_score(forest)