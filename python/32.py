import sys
from typing import List, Tuple
from utils.readfile import readfile_string

if len(sys.argv) < 2:
    print("No file provided")
    exit()

input = list(readfile_string(f"{sys.argv[1]}.txt"))[0]

hex_to_binary_mapping = {
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


def int_to_binary(number: int) -> str:
    binary_string = ""
    while number > 0:
        binary_string = ("0" if number % 2 == 0 else "1") + binary_string
        number = number // 2

    while len(binary_string) < 4:
        binary_string = "0" + binary_string
    return binary_string


def binary_to_int(binary: str) -> int:
    n = pow(2, len(binary) - 1)
    total = 0
    for digit in binary:
        if digit == "1":
            total += n
        n //= 2
    return total


def hex_to_binary(input: str) -> str:
    new_string = ""
    for char in input:
        if char in hex_to_binary_mapping.keys():
            new_string += hex_to_binary_mapping[char]
        else:
            new_string += int_to_binary(int(char))
    return new_string


def process(input: str):
    packet = hex_to_binary(input)
    numbers, _ = process_packet(packet, 0, -1)
    return numbers[0]


def rest_are_zeros(packet, index):
    for digit in packet[index : len(packet) - 1]:
        if digit == "1":
            return False
    return True


def process_packet(packet: str, index: int, number_of_inner_packets: int):
    # print("new", packet, index, number_of_inner_packets)
    step = "version"
    numbers = []
    inner_packet_count = 0
    while index < len(packet):
        print(
            "index:",
            index,
            "needed:",
            number_of_inner_packets,
            "count:",
            inner_packet_count,
        )
        if (
            number_of_inner_packets != -1
            and inner_packet_count == number_of_inner_packets
        ):
            return numbers, index
        if step == "version":
            if rest_are_zeros(packet, index):
                return numbers, index
            index += 3
            step = "type"
        elif step == "type":
            type_id = binary_to_int(packet[index : index + 3])
            # print("type_id:", type_id, "index of type id", index)
            index += 3
            if type_id == 4:
                literal, index = get_literal(packet, index)
                numbers.append(literal)
            else:
                is_type_one = packet[index] == "1"
                index += 1
                type_count_end = index + 11 if is_type_one else index + 15
                length_type_count = binary_to_int(packet[index:type_count_end])
                index += 11 if is_type_one else 15
                packet_to_process = (
                    packet
                    if is_type_one
                    else packet[type_count_end : type_count_end + length_type_count]
                )

                index_to_use = index if is_type_one else 0
                inner_packets, new_index = process_packet(
                    packet_to_process,
                    index_to_use,
                    length_type_count if is_type_one else -1,
                )
                numbers.append(handle_inner_packets(inner_packets, type_id))
                index = new_index if is_type_one else index + length_type_count
            step = "version"
            inner_packet_count += 1
    return numbers, index


def handle_inner_packets(inner_packets: List[int], type_id: int) -> int:
    print(inner_packets, type_id)
    if type_id == 0:
        total = 0
        for number in inner_packets:
            total += number
        return total

    if type_id == 1:
        total = 1
        for number in inner_packets:
            total *= number
        return total

    if type_id == 2:
        minimum = 100000000
        for number in inner_packets:
            minimum = min(minimum, number)
        return minimum

    if type_id == 3:
        maximum = -1
        for number in inner_packets:
            maximum = max(maximum, number)
        return maximum

    if type_id == 5:
        first, second = inner_packets
        return 1 if first > second else 0

    if type_id == 6:
        first, second = inner_packets
        return 1 if first < second else 0

    if type_id == 7:
        first, second = inner_packets
        return 1 if first == second else 0
    return -1


def get_literal(packet: str, index: int) -> Tuple[int, int]:
    binary_string = ""
    while packet[index] == "1":
        binary_string += "".join(packet[index + 1 : index + 5])
        index += 5
    binary_string += "".join(packet[index + 1 : index + 5])
    number = binary_to_int(binary_string)
    print(binary_string, number)
    return number, index + 5


print(process(input))
