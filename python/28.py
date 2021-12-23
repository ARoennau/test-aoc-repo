import sys
from utils.readfile import readfile_string
from collections import defaultdict
from typing import Dict, List, Tuple

if len(sys.argv) < 2:
    print("No file provided")
    exit()

input = list(readfile_string(f"{sys.argv[1]}.txt"))


def split_input(input: List[str]) -> Tuple[List[str], Dict[str, str]]:
    template = [c for c in input[0]]
    rest = input[2:]
    rules: Dict[str, str] = {}
    for line in rest:
        split_rule: List[str] = line.split(" -> ")
        rules[split_rule[0]] = split_rule[1]

    return template, rules


def create_counts(template: List[str], rules: Dict[str, str]) -> Dict[str, int]:
    counts = {}
    for letter in template:
        if letter in counts.keys():
            counts[letter] += 1
        else:
            counts[letter] = 1

    for letter in rules.values():
        if letter not in counts.keys():
            counts[letter] = 0

    return counts


def insertions(input: List[str], steps: int):
    template, rules = split_input(input)
    counts = create_counts(template, rules)
    pairs = defaultdict(int)
    for i in range(0, len(template) - 1):
        pairs[template[i] + template[i + 1]] += 1
    for _ in range(0, steps):
        items = list(pairs.items())
        for pair, count in items:
            pair1 = pair[0] + rules[pair]
            pair2 = rules[pair] + pair[1]
            counts[rules[pair]] += count
            pairs[pair] -= count
            pairs[pair1] += count
            pairs[pair2] += count
    return calculate_difference(counts)


def calculate_difference(counts: Dict[str, int]) -> int:
    min = list(counts.keys())[0]
    max = list(counts.keys())[0]
    for key in counts.keys():
        if counts[key] < counts[min]:
            min = key
        if counts[key] > counts[max]:
            max = key

    return counts[max] - counts[min]


def run_insertion(
    polymer: List[str], counts: Dict[str, int], rules: Dict[str, str]
) -> List[str]:
    insertions: List[Tuple[int, str]] = []
    for i in range(0, len(polymer) - 1):
        group = f"{polymer[i]}{polymer[i + 1]}"
        insertions.append((i + 1, rules[group]))
        counts[rules[group]] += 1

    for i, insertion in enumerate(insertions):
        polymer.insert(insertion[0] + i, insertion[1])

    return polymer


print(insertions(input, 40))
