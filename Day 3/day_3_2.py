from itertools import chain
from string import ascii_lowercase, ascii_uppercase
from collections import Counter


def construct_priority_alphabet_dict() -> dict:
    """

    Construct a dictionary with the given priorities. Lowercase letters - 1 to 26 and uppercase - 27 to 52.
    :return: Return the constructed dictionary

    """
    lowercase: dict = {ascii_lowercase[index]: index + 1 for index in range(len(ascii_lowercase))}
    uppercase: dict = {ascii_uppercase[index]: index + 27 for index in range(len(ascii_uppercase))}
    priority_alphabet: dict = {**lowercase, **uppercase}
    return priority_alphabet


def find_dwarf_group_badges(file_object) -> list:
    """

    A group of dwarfs consists of the 3 consecutive lines in the data file. The badge for this group is determined
    by the one item that is carried by all 3 dwarfs. Return a list with all badges.

    :param file_object: The file object containing all the rucksacks data.
    :return: List with all badges per group.

    """

    data = file_object.readlines()
    badges: list = []
    for index in range(0, len(data), 3):
        first_dwarf: set = set(data[index].strip())
        second_dwarf: set = set(data[index + 1].strip())
        third_dwarf: set = set(data[index + 2].strip())
        frequencies = Counter(chain.from_iterable([first_dwarf, second_dwarf, third_dwarf]))
        badge: str = [index for index in frequencies if frequencies[index] == 3][0]
        badges.append(badge)
    return badges


with open(r"Rucksacks_data", "r") as file:
    priority_alphabet: dict = construct_priority_alphabet_dict()
    badges: list = find_dwarf_group_badges(file_object=file)
    badges_priorities: list = [priority_alphabet[item] for item in badges]
    result: int = sum(badges_priorities)
    print(result)
