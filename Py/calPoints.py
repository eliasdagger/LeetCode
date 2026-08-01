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