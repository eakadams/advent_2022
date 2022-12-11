# code for sorting stacks

with open('test_moves.txt', 'r', encoding="utf-8") as f:
    test_moves = f.readlines()

# read in rucksack contents
with open('moves.txt', 'r', encoding="utf-8") as f:
    moves = f.readlines()

# keep this line uncommented for testing
#content = test_content

test_stacks = [['N', 'Z'],
               ['D','C','M'],
               ['P']]

stacks = [['G','P','N','R'],
          ['H','V','S','C','L','B','J','T'],
          ['L','N','M','B','D','T'],
          ['B','S','P','V','R'],
          ['H','V','M','W','S','Q','C','G'],
          ['J','B','D','C','S','Q','W'],
          ['L','Q','F'],
          ['V','F','L','D','T','H','M','W'],
          ['F','J','M','V','B','P','L']]

# entered stacks wrong so need to reverse
for i in range(len(test_stacks)):
    test_stacks[i].reverse()

for i in range(len(stacks)):
    stacks[i].reverse()

print(test_stacks)

def sort(stacks, moves):
    """Sort stacks using moves"""
    for move in moves:
        remove_move = move.split('move')
        remove_from = remove_move[1].split('from')
        n_move = int(remove_from[0].strip())
        remove_to = remove_from[1].split('to')
        start_stack = int(remove_to[0].strip())
        end_stack = int(remove_to[1].strip())
        for n in range(n_move):
            crate = stacks[start_stack - 1].pop()
            stacks[end_stack-1].append(crate)
    last_crates = ''
    for stack in stacks:
        last_crates += (stack[-1])
    print(last_crates)



sort(test_stacks, test_moves)
sort(stacks, moves)

test_stacks = [['N', 'Z'],
               ['D','C','M'],
               ['P']]

stacks = [['G','P','N','R'],
          ['H','V','S','C','L','B','J','T'],
          ['L','N','M','B','D','T'],
          ['B','S','P','V','R'],
          ['H','V','M','W','S','Q','C','G'],
          ['J','B','D','C','S','Q','W'],
          ['L','Q','F'],
          ['V','F','L','D','T','H','M','W'],
          ['F','J','M','V','B','P','L']]

# entered stacks wrong so need to reverse
for i in range(len(test_stacks)):
    test_stacks[i].reverse()

for i in range(len(stacks)):
    stacks[i].reverse()

def update_sort(stacks, moves):
    """Sort stacks using moves, in one move at once"""
    for move in moves:
        remove_move = move.split('move')
        remove_from = remove_move[1].split('from')
        n_move = int(remove_from[0].strip())
        remove_to = remove_from[1].split('to')
        start_stack = int(remove_to[0].strip())
        end_stack = int(remove_to[1].strip())
        crates = stacks[start_stack-1][-n_move:]
        #print(stacks[start_stack - 1], stacks[end_stack - 1])
        for el in crates:
            stacks[end_stack-1].append(el)
            stacks[start_stack-1].pop()
        #print(stacks[start_stack-1], stacks[end_stack-1])
    last_crates = ''
    for stack in stacks:
        last_crates += (stack[-1])
    print(last_crates)

update_sort(test_stacks, test_moves)
update_sort(stacks, moves)
