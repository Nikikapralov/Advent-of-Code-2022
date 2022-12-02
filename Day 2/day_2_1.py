def get_strategy_guide_data(file_object) -> list:
    """

    Get the list with the strategy guide. A list will be created, with each entry being another list with 2 items,
    our chosen object and the one chosen by the enemy.

    :param file_object: Read file object.
    :return: Return a list with all moves, ours and from our foe as per the strategy guide data.

    """

    data = file_object.readlines()
    clean_of_tabs_data = [item.strip() for item in data]
    strategy_guide_data = [entry.split(" ") for entry in clean_of_tabs_data]
    return strategy_guide_data


def play_round(my_move: str, his_move: str, option_points: dict) -> int:
    """

    Executes a round of Rock, Paper, Scissors, determines the winner and allocates points.
    We have a list with rock, paper and scissors. It is built in such a way, so that each item is beaten by the entry
    that comes after it. For instance, rock is beaten by paper and paper by scissors. If no entry comes after the item,
    like scissors, the list loops and scissors is beaten by rock. We will use this behaviour to determine the winners.

    N.B. Could have used a cycle from itertools, yeah, but I wanted to find a mathematical solution so...I did :)

    :param my_move: The option that I have chosen.
    :param his_move: The option that my opponent has chosen.
    :param option_points: How many points each option gives.
    :return: Return the points I have gained at the end of this round.

    """

    total = 0
    draw = 3
    loss = 0
    win = 6

    rock_paper_scissors = [1, 2, 3]
    index_my_move = rock_paper_scissors.index(option_points[my_move])
    index_his_move = rock_paper_scissors.index(option_points[his_move])
    index_distance = index_my_move - index_his_move
    total += option_points[my_move]

    if index_distance == 0:
        total += draw

    elif index_distance == -1 or index_distance == (len(rock_paper_scissors) - 1):
        total += loss

    elif index_distance == 1 or index_distance == -(len(rock_paper_scissors) - 1):
        total += win

    return total


def get_final_score(strategy_guide: list, option_points: dict) -> int:
    """

    Get the final score of all played games.
    :param strategy_guide: A strategy guide with containing all the outcomes.
    :param option_points: A dictionary mapping different actions to different points.
    :return: The final score after all iterations as an integer.

    """

    total_score = 0
    for his_move, my_move in strategy_guide:
        total_score += play_round(my_move=my_move, his_move=his_move, option_points=option_points)
    return total_score



with open(r".\strategy_guide", "r") as file:
    strategy_guide = get_strategy_guide_data(file_object=file)
    options_points = {"A": 1, "X": 1, "B": 2, "Y": 2, "C": 3, "Z": 3}
    final_score = get_final_score(strategy_guide=strategy_guide, option_points=options_points)
    print(final_score)
