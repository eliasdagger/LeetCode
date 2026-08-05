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