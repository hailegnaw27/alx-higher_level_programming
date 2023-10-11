#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    result = 0
    prev_value = 0
    
    for i in range(len(roman_string) - 1, -1, -1):
        value = roman_values[roman_string[i]]
        
        if value >= prev_value:
            result += value
        else:
            result -= value
        
        prev_value = value
    
    return result


if __name__ == "__main__":
    roman_number = "X"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "VII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "IX"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "LXXXVII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "DCCVII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))
