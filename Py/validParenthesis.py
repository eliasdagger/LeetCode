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

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = list(s)
        i = 0
        st = []
        
        while i < len(l):
            if l[i] == "[" or l[i] == "(" or l[i] == "{":
                st.append(l[i])
                i += 1
            else:
                if not st:
                    return False
                peek = st[len(st) -1]
                if (peek == "("  and l[i] == ")") or (peek == "[" and l[i] == "]") or (peek == "{" and l[i] == "}"):
                    st.pop()
                    i +=1
                    continue
                else: 
                    return False
        return len(st) == 0
        