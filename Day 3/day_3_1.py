from string import ascii_lowercase, ascii_uppercase


def construct_priority_alphabet_dict() -> dict:
    """

    Construct a dictionary with the given priorities. Lowercase letters - 1 to 26 and uppercase - 27 to 52.
    :return: Return the constructed dictionary

    """
    lowercase: dict = {ascii_lowercase[index]: index + 1 for index in range(len(ascii_lowercase))}
    uppercase: dict = {ascii_uppercase[index]: index + 27 for index in range(len(ascii_uppercase))}
    priority_alphabet: dict = {**lowercase, **uppercase}
    return priority_alphabet


def find_repeated_items_in_compartments(file_object) -> list:
    """

    Find all repeated items in compartments. For each backpack, check which items are to be found in both compartments,
    get their priority values and save them in a list. Return the list.

    :param file_object: The file object containing all the rucksacks data.
    :return: List with priority values of all items that are to be found in both compartments.

    """

    data = file_object.readlines()
    items_in_both_compartments_across_all_backpacks: list = []
    for backpack_info in data:
        backpack_info: str = backpack_info.strip()
        first_compartment: set = set(backpack_info[0:len(backpack_info) // 2])
        second_compartment: set = set(backpack_info[len(backpack_info) // 2:])
        items_in_both_compartments: set = first_compartment.intersection(second_compartment)
        items_in_both_compartments_across_all_backpacks.append(*items_in_both_compartments)
    return items_in_both_compartments_across_all_backpacks



with open(r"Rucksacks_data", "r") as file:
    priority_alphabet: dict = construct_priority_alphabet_dict()
    repeated_items: list = find_repeated_items_in_compartments(file_object=file)
    repeated_items_priorities: list = [priority_alphabet[item] for item in repeated_items]
    result: int = sum(repeated_items_priorities)
    print(result)
