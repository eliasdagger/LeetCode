class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        # in order to ensure that all instances of y occur before x in our result, for count of y, add to string first, then add the rest of the chars in string skipping the y's
        res = ""
        c = collections.Counter(s)
        
        for ss in range(c[y]):
            res += y
            
        for ch in s:
            if ch == y:
                continue
            else:
                res += ch

        return res