
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