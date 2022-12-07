# scripts to count calories

# read elf holding information in
with open('elf_calories.txt', 'r', encoding="utf-8") as f:
    elf_data = f.readlines()

# now loop through to do calorie count
calorie_per_elf = []
cal_count = 0
for cookie in elf_data:
    if cookie is '\n':
        # end of elf, reset things
        calorie_per_elf.append(cal_count)
        cal_count = 0
    else:
        # have something to add to count
        cal_count = cal_count + int(cookie)

# find maximum calorie count
max_cals = max(calorie_per_elf)
print(f"Max calories an elf is carrying is {max_cals}")

# find which elf has this
# must be a smarter way to do this!
for elf, cal in enumerate(calorie_per_elf):
    if cal == max_cals:
        print(f"Elf at index {elf}, or the {elf+1}th elf has the max cals {max_cals}")

# find how many calories there are total between the top three elves
calorie_pe r_elf.sort()
top_three_total = sum(calorie_per_elf[-3:])

print(f"The top three elves are carrying {top_three_total} calories")