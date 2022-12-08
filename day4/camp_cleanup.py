# code for camp cleanup

with open('test_pairs.txt', 'r', encoding="utf-8") as f:
    test_pairs = f.readlines()

# read in rucksack contents
with open('cleaning_pairs.txt', 'r', encoding="utf-8") as f:
    pairs = f.readlines()

# keep this line uncommented for testing
#pairs = test_pairs

#print(pairs)

fully_redundant_pairs = 0
partially_redundant_pairs = 0
for elf_pair in pairs:
    # first strip newline
    stripped_pair = elf_pair.rstrip()
    # then split on comma
    split_pair = stripped_pair.split(',')
    #print(split_pair)
    # then for each half of pair, split on dah to get range
    elf_a_range = split_pair[0].split('-')
    elf_b_range = split_pair[1].split('-')
    elf_a_start = int(elf_a_range[0])
    elf_a_end = int(elf_a_range[1])
    elf_b_start = int(elf_b_range[0])
    elf_b_end = int(elf_b_range[1])
    print(stripped_pair, elf_a_start, elf_a_end, elf_b_start, elf_b_end)
    # check if b is fully in a:
    if (elf_b_start >= elf_a_start) and (elf_a_start <= elf_b_end <= elf_a_end):
        fully_redundant_pairs = fully_redundant_pairs + 1
        print(stripped_pair)
    # check if a is fully within b:
    elif (elf_a_start >= elf_b_start) and (elf_b_start <= elf_a_end <= elf_b_end):
        fully_redundant_pairs = fully_redundant_pairs + 1
        print(stripped_pair)
    # check if there is partial overlap
    # how can partial overlap happen? start or end of one pair within middle of other pair
    if elf_a_start <= elf_b_start <= elf_a_end:
        partially_redundant_pairs = partially_redundant_pairs + 1
    elif elf_a_start <= elf_b_end <= elf_a_end:
        partially_redundant_pairs = partially_redundant_pairs + 1
    elif elf_b_start <= elf_a_start <= elf_b_end:
        partially_redundant_pairs = partially_redundant_pairs + 1
    elif elf_b_start <= elf_a_end <= elf_b_end:
        partially_redundant_pairs = partially_redundant_pairs + 1

print(f'The number of fully redundant pairs is {fully_redundant_pairs}')
print(f'The number of partially redundant pairs is {partially_redundant_pairs}')