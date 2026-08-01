class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        # convert n to string to iterate each digit, use collections counter to count each char conv into a key value pair {'char': frequency}. simple for loop .items() to handle key value pairs. then perform the arithmetic the problem requires
        s = str(n)
        res = 0
        c = collections.Counter(s)
        
        for key, value in c.items():
            res += int(key) * value

        return res

        