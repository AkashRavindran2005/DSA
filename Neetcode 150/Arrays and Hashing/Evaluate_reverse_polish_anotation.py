class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in '+-*/':
                second = int(stack.pop())
                first = int(stack.pop())
                if i == '+':
                    stack.append(first + second)
                if i == '-':
                    stack.append(first - second)
                if i == '*':
                    stack.append(first * second)
                if i == '/':
                    stack.append(first / second)
            else:
                stack.append(i)
        return int(stack[0])