# Перевод римских чисел в арабские

def roman_numbers(roman):

    all_numbers = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }

    all_negative_numbers = {
        'IV':4,
        'IX':9,
        'XL':40,
        'XC':90,
        'CD':400,
        'CM':900
    }

    arabian = 0
    new_string = roman.upper()

    for k in all_negative_numbers.keys():
        if k in new_string:
            arabian += all_negative_numbers[k]
            new_string = new_string.replace(k,'')
            roman_numbers(new_string)

    for k in new_string:
        if k in all_numbers:
            arabian += all_numbers[k]
        else:
            return 0


    return arabian


print(roman_numbers('MMXXII'))
