# code for getting into rucksack contents

# read in test rucksack contents
import string

with open('test_content.txt', 'r', encoding="utf-8") as f:
    test_content = f.readlines()

# read in rucksack contents
with open('rucksack_contents.txt', 'r', encoding="utf-8") as f:
    content = f.readlines()

# keep this line uncommented for testing
#content = test_content

priority = 0
priority_string = string.ascii_lowercase + string.ascii_uppercase
print(priority_string)
for rucksack in content:
    # string includes new line character
    total_items = len(rucksack) - 1
    #print(f"Rucksack {rucksack} has {total_items} total items")
    compartment_a = rucksack[0:int(total_items/2)]
    compartment_b = rucksack[int(total_items/2):total_items]
    #print(f"Compartment a is {compartment_a} and compartment b is {compartment_b}")
    for item in compartment_a:
        if item in compartment_b:
            #print(f"Item {item} is in compartment a and b")
            duplicate_item = item
            break
    # can i be smarter and do the above with list comprehension?
    # probably.....
    # how do i assign priority? that's what i'm struggling wtih
    # maybe a string where I can match index, use that index for priority...
    priority = priority + priority_string.find(item) + 1

print(f"The total priority of mispacked items is {priority}")

# then start getting badges
badge_priority = 0
ngroups = int((len(content)/3))
for group in range(ngroups):
    group_contents = content[int(group*3):int(group*3+3)]
    # then find common element
    # compare first rucksack to second
    # if successful compare to third, break if works
    # otherwise keep going with first comparison
    for item in group_contents[0]:
        if item in group_contents[1]:
            if item in group_contents[2]:
                badge = item
                break
    #print(f"The badge for group {group} is {item}")
    badge_priority = badge_priority + priority_string.find(item) + 1

print(f"The total priority of badges is {badge_priority}")
