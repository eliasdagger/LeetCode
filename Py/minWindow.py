class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        # create left and right pointers, every number is less than infinity so comparing to inf will readjust minimum substring
        res, resLen = [-1,-1], float("infinity")
        l = 0
        # Create two dcts, here we can count frequency of the chars of t and if they match to s substring
        countT, window = {}, {}

        # count frequencies
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        # we need to find len(countT) in our window, this counts the unique keys in the dct
        have, need = 0, len(countT)

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            # we want to have 
            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    # readjust res
                    res = [l, r]
                    resLen = r - l + 1

                # removing a char from the window while readjusting the window, decrement the counter, if this was a "need" char, and now the window has less than we "need" decrement have and shift left pointer. 
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1

                l += 1
        # if the string hasnt been changed != inf, then return our pointers else, it doesnt exist thus return ""
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""