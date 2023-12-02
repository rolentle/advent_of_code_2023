import re

def day_1(input: str) -> int:
    print("day 1")
    return sum(day_1_input_into_digits(input))

def numberize(input: str) -> int:
    match input:
        case 'one':
            return '1'
        case 'two':
            return '2'
        case 'three':
            return '3'
        case 'four':
            return '4'
        case 'five':
            return '5'
        case 'six':
            return '6'
        case 'seven':
            return '7'
        case 'eight':
            return '8'
        case 'nine':
            return '9'
        case _:
            return input

def day_1_input_into_digits(input: str) -> list[str]:
    results = []
    for line in input.split("\n"):
        numbers = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
        print(numbers)
        first_and_last_numbers = [numbers[0], numbers[-1]]
        number = ''.join(map(numberize, first_and_last_numbers))
        results.append(int(number))
    
    return results
        

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

