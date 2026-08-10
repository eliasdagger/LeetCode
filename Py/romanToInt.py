# LeetCode 13 - Roman to Integer (Easy)
#
# Roman numerals use the symbols I(1) V(5) X(10) L(50) C(100) D(500) M(1000),
# normally written from largest to smallest and simply added up.
#
# Six cases are written subtractively instead, putting the smaller symbol first:
#   IV = 4    IX = 9
#   XL = 40   XC = 90
#   CD = 400  CM = 900
#
# Given a roman numeral string s, return the integer it represents. The input is
# guaranteed to be a valid numeral somewhere in the range 1 to 3999.
#
# Example: 'MCMXCIV'  ->  1994 (M=1000, CM=900, XC=90, IV=4)


def romanToInt(s):
    # init count to 0, create a dictionary of roman numerals and their respective values
    c = 0
    dct = {"I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900}
    # left pointer as we read left to right
    l = 0
    while l < len(s):
        # check for two char nums handle those, if used move pointer by 2, else handle single char nums and move pointer by 1
        if s[l:l+2] in dct:
            c += dct.get(s[l:l+2], 0)
            l += 2
        else:
            c += dct.get(s[l], 0)
            l += 1
    
    return c