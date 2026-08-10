# LeetCode 682 - Baseball Game (Easy)
#
# You are keeping score for a game with unusual rules. You are given a list of
# string operations, applied in order to a record of scores:
#
#   an integer x  record a new score of x
#   '+'           record a new score equal to the sum of the previous two scores
#   'D'           record a new score equal to double the previous score
#   'C'           invalidate the previous score, removing it from the record
#
# Return the sum of all the scores still on the record once every operation has
# been applied. Every operation is guaranteed to be valid at the point it appears.
#
# Example: ['5','2','C','D','+']  ->  30

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []

        # follow baseball game rules, else condition will ensure any int is handled rather than an if statement with a tedious condition
        for op in operations:
            if op == '+':
                res.append(res[-1] + res[-2])
            elif op == 'D':
                res.append(res[-1] * 2)
            elif op == 'C':
                res.pop()
            else:
                res.append(int(op))
        return sum(res)