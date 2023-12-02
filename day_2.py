import pytest
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


# Test
f = open("./fixtures/day_2_sample.txt")
day_2_sample_data = f.read()
bag_data = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def test_day_2_part_1_sample():
    assert day_2(day_2_sample_data, bag_data) == 8

def test_day_2_part_1():
    f = open("./fixtures/day_2_part_1.txt")
    day_2_data = f.read()
    assert day_2(day_2_data, bag_data) == 3099

def test_parse_day_2_line_data():
    game_1_text = day_2_sample_data.split("\n")[0]
    expected_game_1_data = {
        "id": 1,
        "sets": [
            {
                "blue": 3,
                "red": 4,
            },
            {
                "red": 1,
                "green": 2,
                "blue": 6,
            },
            {
                "green": 2,
            }
        ]
    }

    assert parse_day_2_line_data(game_1_text) == expected_game_1_data


def test_valid_day_2_game_data():
    expected_game_1_data = {
        "id": 1,
        "sets": [
            {
                "blue": 3,
                "red": 4,
            },
            {
                "red": 1,
                "green": 2,
                "blue": 6,
            },
            {
                "green": 2,
            }
        ]
    }

    assert valid_day_2_game_data(expected_game_1_data, bag_data) == True

def test_invalid_day_2_game_data():
    expected_game_3_data = {
        "id": 3,
        "sets": [
            {
                "green": 8,
                "blue": 6,
                "red": 20,
            },
            {
                "blue": 5,
                "red": 4,
                "green": 13,
            },
            {
                "red": 1,
                "green": 5,
            }
        ]
    }

    assert valid_day_2_game_data(expected_game_3_data, bag_data) == False

def test_fewest_dice_possible():
    expected_game_1_data = {
        "id": 1,
        "sets": [
            {
                "blue": 3,
                "red": 4,
            },
            {
                "red": 1,
                "green": 2,
                "blue": 6,
            },
            {
                "green": 2,
            }
        ]
    }
    assert fewest_dice_possible(expected_game_1_data) == { "blue": 6, "red": 4, "green": 2}


def test_game_power():
    expected_game_1_data = {
        "id": 1,
        "sets": [
            {
                "blue": 3,
                "red": 4,
            },
            {
                "red": 1,
                "green": 2,
                "blue": 6,
            },
            {
                "green": 2,
            }
        ]
    }
    assert game_power(expected_game_1_data) == 48

def test_day_2_part_2_sample():
    assert day_2_part_2(day_2_sample_data) == 2286

def test_day_2_part_2():
    f = open("./fixtures/day_2_part_1.txt")
    day_2_data = f.read()
    assert day_2_part_2(day_2_data) == 72970