# LeetCode 20 - Valid Parentheses (Easy)
#
# Given a string s containing only the characters '(', ')', '{', '}', '[' and ']',
# decide whether it is valid.
#
# A string is valid when every open bracket is closed by a bracket of the same
# type, brackets close in the correct order, and every closing bracket has a
# matching open bracket waiting for it. A string that ends with brackets still
# open is not valid either.
#
# Example: '()[]{}'  ->  true
#          '(]'      ->  false
#          '([)]'    ->  false (right types, wrong order)
#          '{[]}'    ->  true

class Solution:
    def isValid(self, s: str) -> bool:
        # Any odd length is not closable since it wont have sufficient corresponding closing parenthesis for its opening parenthesis or vice versa. 
        if len(s) % 2 != 0: return False

        stack = []
        dct = {
            ")": "(",
            "]": "[",
            "}": "{" 
        }
        # if our char in a value in our dct, append as it is an opening bracket, else we will check if the left most bracket that hasnt been check is its correspondant.
        for char in s:
            if char in dct.values():
                stack.append(char)
            else:
                if not stack or stack.pop() != dct[char]:
                    return False
        # return if the stack is empty this covers cases like "][][]"
        return not stack
        