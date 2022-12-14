from collections import deque


def get_calories_dict(file_object) -> dict:
    """
    Get a dictionary with entries for each elf and his food items.
    Elfs are now dwarfs. Iterate through the file data in a queue manner (Yeah, I know we really don't need a queue but
    I wanted to use one so I did...)
    and check if each food item is actually food
    or a delimiter. If food, add to the dictionary, otherwise if delimiter, add new dwarf to dictionary and continue.
    :param file_object: The file with the data.
    :return: Return a dictionary with the data.
    """

    calories_dict = {}
    data = deque(file_object.readlines())
    dwarf_number = 1
    current_dwarf = f"Dwarf_{dwarf_number}"
    calories_dict[current_dwarf] = []

    while data:
        entry = data.popleft()
        if is_food_item(entry):
            calories_dict[current_dwarf].append(int(entry.strip()))
        else:
            dwarf_number += 1
            current_dwarf = f"Dwarf_{dwarf_number}"
            calories_dict[current_dwarf] = []

    return calories_dict


def is_food_item(entry: str) -> bool:
    """
    Check if the current entry is a food item or a delimiter.
    :param entry: The current entry, foot item or delimiter.
    :return: Return a boolean True/False
    """
    return entry[0].isnumeric()


def calculate_total_calories(calories_dict: dict) -> dict:
    """
    Get total calories from all food items per dwarf.
    :param calories_dict: Dictionary with dwarfs and their food items.
    :return: Return a new dictionary with dwarfs and their total calories.
    """
    return {dwarf: sum(food_items) for dwarf, food_items in calories_dict.items()}


def get_most_calories(total_calories_dict: dict) -> int:
    """
    Reorder the dictionary such as the first entry to be the dwarf with the most calories, then return the amount of
    calories as an integer.
    :param total_calories_dict: Dictionary with dwarfs and their total amount of calories
    :return: Returns a single integer, the most calories carried by a dwarf.
    """
    ordered_calories = sorted(total_calories_dict.items(), key=lambda x: x[1], reverse=True)
    most_calories = ordered_calories[0][1]
    return most_calories


with open(r"./calories_data", "r") as file:
    calories_dict = get_calories_dict(file_object=file)
    total_calories_dict = calculate_total_calories(calories_dict=calories_dict)
    most_calories = get_most_calories(total_calories_dict=total_calories_dict)
    print(most_calories)



