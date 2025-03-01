def int_to_roman(num):
    """
    Convert an integer to a Roman numeral.

    :param num: Integer value between 1 and 3999 inclusive.
    :return: A string representing the Roman numeral of the integer.
    """
    roman_symbol_values = [(1, "I" ), (5, "V"), (4,"IV"), (10, "X"), 
        (9,"IX"), (50, "L"), (40,"XL"), (100, "C"), (90,"XC"),
        (500, "D"), (400, "CD"), (1000,"M"), (900, "CM")]

    roman_symbol_values.sort(reverse=True, key=lambda  x:x[0]) 
    result= ""

    for value, symbol in roman_symbol_values:
        while num>= value:
            result += symbol
            num-= value
        
    return result