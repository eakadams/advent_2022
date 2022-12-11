# code for exploring file system
# used solutions to help me with this one a bit
# i defintiely struggled!
with open('terminal_output.txt', 'r', encoding="utf-8") as f:
    s = f.read()
    output = s.split('\n')

with open('test_terminal_output.txt', 'r', encoding="utf-8") as f:
    s = f.read()
    test_output = s.split('\n')


def get_folder_sizes(output):
    """ Return a dict of folder sizes from commands """
    folders = {}
    path = ['/']
    current_path = ''.join(path)
    folders.setdefault(current_path, 0)

    for line in output:
        line = line.strip('$ ').split()
        if line[0] == 'ls':
            pass
        elif line[0] == "dir":
            folders.setdefault(current_path + line[1] + '/', 0)
        elif line[0].isdigit():
            folders[current_path] += int(line[0])
        elif line[0] == 'cd':
            if line[1] == '/':
                path = [line[1]]
                current_path = ''.join(path)
            elif line[1] == '..':
                subfolder_size = folders.get(current_path)
                path.pop()
                current_path = ''.join(path)
                folders[current_path] += subfolder_size
            else:
                path.append(line[1] + '/')
                current_path = ''.join(path)

    # account for anything still in stack
    for n in range(len(path) - 1):
        subfolder_size = folders.get(current_path)
        path.pop()
        current_path = ''.join(path)
        folders[current_path] += subfolder_size

    return folders


test_folders = get_folder_sizes(test_output)


def get_small_dirs(folders):
    """get sum of directories less than 100000"""
    sum = 0
    for size in folders.values():
        if size < 100000:
            sum += size
    print(f'Sum of folders less than 100000 is {sum}')

get_small_dirs(test_folders)

folders = get_folder_sizes(output)
get_small_dirs(folders)

total_disk_space = 70000000
needed_disk_space = 30000000


def find_directory_to_delete(folders):
    """Find smallest possible directory to create needed space"""
    total_disk_space = 70000000
    needed_disk_space = 30000000
    total_used_disk_space = folders['/']
    unused_disk_space = total_disk_space - total_used_disk_space
    min_size_to_delete =  needed_disk_space - unused_disk_space
    return min(v for v in folders.values() if v > min_size_to_delete)

test_size_delete = find_directory_to_delete(test_folders)
size_delete = find_directory_to_delete(folders)

print(f'The size of directory to delete from the test is {test_size_delete}')
print(f'The size of directory to delete is {size_delete}')
