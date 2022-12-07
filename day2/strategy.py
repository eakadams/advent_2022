# code to test RPS strategy

# read strategy information in
with open('rps_guide.txt', 'r', encoding="utf-8") as f:
    rps_moves = f.readlines()


# read test info in
with open('test_rps.txt', 'r', encoding="utf-8") as f:
    test_rps_moves = f.readlines()


# get score
score = 0
for turn in rps_moves:
    # limited possibilities, so test each
    if turn == 'A X\n':
        score = score + 1 + 3
    elif turn == 'A Y\n':
        score = score + 2 + 6
    elif turn == 'A Z\n':
        score = score + 3 + 0
    elif turn == 'B X\n':
        score = score + 1 + 0
    elif turn == 'B Y\n':
        score = score + 2 + 3
    elif turn == 'B Z\n':
        score = score + 3 + 6
    elif turn == 'C X\n':
        score = score + 1 +6
    elif turn == 'C Y\n':
        score = score + 2 + 0
    elif turn == 'C Z\n':
        score = score + 3 + 3
    else:
        print('Warning! No score')

print(f"Total score is {score}.")

# get score for updated strategy
# A, B, C = rock, paper scissor (1, 2, 3)
# X, Y, Z = lose, draw, win (0, 3, 6)
new_score = 0
for turn in rps_moves:
    # limited possibilities, so test each
    if turn == 'A X\n':
        new_score = new_score + 3 + 0
    elif turn == 'A Y\n':
        new_score = new_score + 1 + 3
    elif turn == 'A Z\n':
        new_score = new_score + 2 + 6
    elif turn == 'B X\n':
        new_score = new_score + 1 + 0
    elif turn == 'B Y\n':
        new_score = new_score + 2 + 3
    elif turn == 'B Z\n':
        new_score = new_score + 3 + 6
    elif turn == 'C X\n':
        new_score = new_score + 2 +0
    elif turn == 'C Y\n':
        new_score = new_score + 3 + 3
    elif turn == 'C Z\n':
        new_score = new_score + 1 + 6
    else:
        print('Warning! No score')

print(f"Total score with new strategy is {new_score}.")