import pytest
import re

def day_2(input: str, bag_data: dict)-> int:
    total = 0

    for game_text in input.split("\n"):
        game_data = parse_day_2_line_data(game_text)
        if valid_day_2_game_data(game_data, bag_data):
            total += game_data["id"]
    
    return total


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

