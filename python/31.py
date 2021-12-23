import sys
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
    total, _ = process_packet(packet, 0, -1)
    return total


def rest_are_zeros(packet, index):
    for digit in packet[index : len(packet) - 1]:
        if digit == "1":
            return False
    return True


def process_packet(packet: str, index: int, number_of_inner_packets: int):
    # print("new", packet, index, number_of_inner_packets)
    step = "version"
    total = 0
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
            return total, index
        if step == "version":
            version = binary_to_int(packet[index : index + 3])
            # print("version", version)
            if rest_are_zeros(packet, index):
                # print("rest are zeroes")
                return total, index
            total += version
            index += 3
            step = "type"
        elif step == "type":
            type_id = binary_to_int(packet[index : index + 3])
            # print("type_id:", type_id, "index of type id", index)
            index += 3
            if type_id == 4:
                index = find_end_of_literal(packet, index)
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
                inner_total, new_index = process_packet(
                    packet_to_process,
                    index_to_use,
                    length_type_count if is_type_one else -1,
                )
                total += inner_total
                index = new_index if is_type_one else index + length_type_count
            step = "version"
            inner_packet_count += 1
    return total, index


def find_end_of_literal(packet: str, index: int) -> int:
    while packet[index] == "1":
        index += 5
    return index + 5


print(process(input))
