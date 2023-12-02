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
        
