import sys
from utils.readfile import readfile_string

if len(sys.argv) < 2:
    print('No file provided')
    exit()

input = list(readfile_string(f'{sys.argv[1]}.txt'))


def generate_adjacency_list(input):
    adjacency_list = {}
    for line in input:
        start, end = line.split('-')
        if start != 'end':
            if start in adjacency_list.keys():
                adjacency_list[start].append(end)
            else:
                adjacency_list[start] = [end]

        if end != 'end':
            if end in adjacency_list.keys() and end != 'end':
                adjacency_list[end].append(start)
            else:
                adjacency_list[end] = [start]

    return adjacency_list


def find_paths(input):
    adjacency_list = generate_adjacency_list(input)
    return find_path_total(adjacency_list, ['start'])


def find_path_total(adjacency_list, current_path):
    current_node = current_path[-1]

    if current_node not in adjacency_list.keys():
        current_path.pop()
        return 1 if current_node == 'end' else 0

    if current_node.islower() and current_node in current_path[:-1]:
        current_path.pop()
        return 0

    total = 0
    for node in adjacency_list[current_node]:
        if node == 'start':
            continue
        current_path.append(node)
        total += find_path_total(adjacency_list, current_path)

    current_path.pop()

    return total


print(find_paths(input))
