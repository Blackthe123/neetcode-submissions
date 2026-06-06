class Solution:
    def isValid(self, s: str) -> bool:
        openb = "({["
        closeb = ")}]"
        mapping = {')': '(', '}':'{', ']':'['}
        stack = []
        for i in range(len(s)):
            if s[i] in openb:
                stack.append(s[i])
            if s[i] in closeb:
                if len(stack) > 0 and mapping[s[i]] == stack[-1]:
                    stack.pop()
                else:
                    return False
        if len(stack) > 0:
            return False
        return True
            
        