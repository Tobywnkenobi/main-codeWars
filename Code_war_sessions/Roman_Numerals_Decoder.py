'''
Create a function that takes a Roman numeral as its argument and returns its value as a numeric decimal integer. You don't need to validate the form of the Roman numeral.

Modern Roman numerals are written by expressing each decimal digit of the number to be encoded separately, starting with the leftmost digit and skipping any 0s. So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC) and 2008 is rendered "MMVIII" (2000 = MM, 8 = VIII). The Roman numeral for 1666, "MDCLXVI", uses each letter in descending order.
Example:

"MM"      -> 2000
"MDCLXVI" -> 1666
"M"       -> 1000
"CD"      ->  400
"XC"      ->   90
"XL"      ->   40
"I"       ->    1

'''

def solution(roman: str) -> int:
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    total = 0
    prev_value = 0

    for char in roman[::-1]:
        cur_value = roman_values[char]
        if cur_value < prev_value:
            total -= cur_value
        else:
            total += cur_value

        prev_value = cur_value

    return total

print(solution("MM"))      # Output: 2000
print(solution("MDCLXVI")) # Output: 1666
print(solution("M"))       # Output: 1000
print(solution("CD"))      # Output: 400
print(solution("XC"))      # Output: 90
print(solution("XL"))      # Output: 40
print(solution("I"))       # Output: 1