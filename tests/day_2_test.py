import pytest

from aoc.day_2 import *

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