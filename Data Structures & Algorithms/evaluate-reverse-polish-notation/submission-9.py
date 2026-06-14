class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if any(char.isdigit() for char in tokens[i]):
                stack.append(int(tokens[i]))
            elif tokens[i] == '+':
                stack.append(stack.pop() + stack.pop())
            elif tokens[i] == '-':
                stack.append(stack.pop(-2) - stack.pop())
            elif tokens[i] == '*':
                stack.append(stack.pop() * stack.pop())
            else:
                stack.append(int(stack.pop(-2) / stack.pop()))
            print(stack)
        return stack.pop()