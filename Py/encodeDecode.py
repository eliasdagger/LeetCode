# LeetCode 271 - Encode and Decode Strings (Medium, premium)
#
# Design an algorithm that serializes a list of strings into one single string
# that could be sent over a network, and then deserializes that string back into
# the exact original list.
#
#   encode(strs)  ->  a single string
#   decode(s)     ->  the original list of strings
#
# The catch is that the strings may contain any characters at all, including
# whatever delimiter you were planning to join on, so a plain "join with a comma"
# breaks. The standard fix is to prefix each string with its own length and a
# marker character, e.g. ['lint','code'] encodes as '4#lint4#code' - the decoder
# reads the number, so it knows exactly how many characters to take next and never
# has to guess where a string ends.

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j+1+length])
            i = j + 1 + length
        return res