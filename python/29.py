import sys
from utils.readfile import readfile_string

from collections import defaultdict
from typing import List, Tuple


class PriorityQueue:
    queue = []

    def add(self, point: Tuple[Tuple[int, int], int, List[Tuple[int, int]]]):
        self.queue.append(point)
        self.__heap_up(len(self.queue) - 1)

    def remove(self, point: Tuple[Tuple[int, int], int, List[Tuple[int, int]]]):
        self.queue.remove(point)

    def __swap(self, a: int, b: int):
        temp = self.queue[a]
        self.queue[a] = self.queue[b]
        self.queue[b] = temp

    def __heap_up(self, index: int):
        while True:
            if index == 0:
                break
            parent_index = (index - 1) // 2
            if self.queue[index][1] < self.queue[parent_index][1]:
                self.__swap(index, parent_index)
                index = parent_index
            else:
                break

    def __heap_down(self, index: int):
        while True:
            if index >= len(self.queue):
                break
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            if left_child_index >= len(self.queue):
                break
            min_index = -1
            if right_child_index == len(self.queue):
                min_index = left_child_index
            else:
                if (
                    self.queue[index][1] < self.queue[left_child_index][1]
                    and self.queue[index][1] < self.queue[right_child_index][1]
                ):
                    break
                min_index = (
                    left_child_index
                    if self.queue[left_child_index][1]
                    < self.queue[right_child_index][1]
                    else right_child_index
                )
            if self.queue[index][1] > self.queue[min_index][1]:
                self.__swap(index, min_index)
                index = min_index
            else:
                break

    def pop(self):
        min = self.queue[0]
        self.__swap(0, len(self.queue) - 1)
        del self.queue[len(self.queue) - 1]
        if len(self.queue) > 0:
            self.__heap_down(0)
        return min

    def is_empty(self):
        return len(self.queue) == 0


if len(sys.argv) < 2:
    print("No file provided")
    exit()

input = list(readfile_string(f"{sys.argv[1]}.txt"))


def form_array(input: List[str]) -> List[List[int]]:
    array = []
    for row in input:
        split_row = [num for num in row]
        array.append(list(map(lambda str: int(str), split_row)))
    return array


def find_shortest_path(input: List[str]):
    array = form_array(input)
    queue = PriorityQueue()
    dict = defaultdict(lambda: 1000000)
    dict_path = defaultdict(list)
    queue.add(((0, 1), 0, [(0, 0)]))
    queue.add(((1, 0), 0, [(0, 0)]))

    while not queue.is_empty():
        coords, distance, path = queue.pop()
        x, y = coords
        if dict[(x, y)] < 100000:
            continue
        dict[(x, y)] = distance
        dict_path[(x, y)] = path
        new_path = path.copy()
        new_path.append((x, y))
        for i in (-1, 1):
            if x + i >= 0 and x + i < len(array[0]) and (x + i, y) != (0, 0):
                queue.add(((x + i, y), distance + array[y][x], new_path))
            if y + i >= 0 and y + i < len(array) and (x, y + i) != (0, 0):
                queue.add(((x, y + i), distance + array[y][x], new_path))

    return (
        dict[(len(array) - 1, len(array[0]) - 1)]
        + array[len(array) - 1][len(array[0]) - 1]
    )


print(find_shortest_path(input))
