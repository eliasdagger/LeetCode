# LeetCode 150 - Evaluate Reverse Polish Notation (Medium)
#
# You are given an array tokens holding an arithmetic expression written in
# Reverse Polish Notation, where each operator comes after its two operands
# instead of between them.
#
# Evaluate the expression and return the integer result. Valid operators are '+',
# '-', '*' and '/'; every other token is an integer. Division between two integers
# truncates toward zero, there is never a division by zero, and the expression is
# always valid.
#
# Example: ['2','1','+','3','*']  ->  ((2 + 1) * 3) = 9
#          ['4','13','5','/','+'] ->  (4 + (13 / 5)) = 6

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Create a stack, create our lambda functions, for each index in the tokens list, we will eval them as a number or an operation, if its an operation we will take the last two numbers from the stack and apply the operation (with b being the top of the stack and a second top to maintain left to right reading the operations of math)
        # it its not an operation will we will add it to the stack as an int to operate on it later. 
        # return the final int with stack.pop()
        stack = []

        ops = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b)
        }

        for token in tokens: 
            if token in ops:
                b = stack.pop()
                a = stack.pop()
            
                stack.append(ops[token](a,b))

            else:
                stack.append(int(token))

        return stack.pop()