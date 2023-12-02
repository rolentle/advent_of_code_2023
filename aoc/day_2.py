import re

def day_2(input: str, bag_data: dict)-> int:
    total = 0

    for game_text in input.split("\n"):
        game_data = parse_day_2_line_data(game_text)
        if valid_day_2_game_data(game_data, bag_data):
            total += game_data["id"]
    
    return total

def day_2_part_2(input: str)-> int:
    power = 0
    for game_text in input.split("\n"):
        game_data = parse_day_2_line_data(game_text)
        power += game_power(game_data)

    return power



def parse_day_2_line_data(input: str)-> dict:
    game_id_text, set_text = input.split(":")
    game_id = int(re.findall(r'Game (\d+)$', game_id_text)[0])
    game_sets = []
    for individual_set in set_text.split(";"):
        game_set = {}
        for dice_amount in individual_set.split(","):
            amount, dice_color = dice_amount.strip().split(" ")
            game_set[dice_color] = int(amount)
        
        game_sets.append(game_set)

    
    return { 
        "id": game_id,
        "sets": game_sets
    }


def valid_day_2_game_data(game_data: dict, bag_data: dict)-> bool:
    game_sets = game_data["sets"]
    
    for game_set in game_sets:
        for dice_color in bag_data:
            if game_set.get(dice_color, 0) > bag_data[dice_color]: 
                return False

    return True

def fewest_dice_possible(game_data: dict)-> dict:
    fewest_dice_possible = {}
    print(game_data)
    for game_set in game_data["sets"]:
        for dice_color in game_set:
            if game_set[dice_color] > fewest_dice_possible.get(dice_color, 0):
                fewest_dice_possible[dice_color] = game_set[dice_color]

    return fewest_dice_possible


def game_power(game_data: dict)-> int:
    power = 1
    for value in fewest_dice_possible(game_data).values():
        power *= value

    return power