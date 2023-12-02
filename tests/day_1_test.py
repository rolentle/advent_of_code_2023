import pytest

from aoc.day_1 import(
    day_1,
    day_1_input_into_digits,
)

day_1_part_2_sample_input = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

def test_day_1_part_2_input_into_digits():
    assert day_1(day_1_part_2_sample_input) == 281

day_1_sample_input = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

def test_day_1_sample():
    assert day_1(day_1_sample_input) == 142 

def test_day_1_part_1():
    f = open("fixtures/day_1_part_1.txt", "r") 
    answer = day_1(f.read())
    assert answer == 54431

def test_convert_day_1_input_into_digits():
    assert day_1_input_into_digits(day_1_sample_input) == [12, 38, 15, 77]
