class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0 for _ in range(len(temperatures))]
        stack = []
        for i in range(len(temperatures)):
            if not stack or temperatures[stack[-1]] > temperatures[i]:
                stack.append(i)
            else:
                while stack and temperatures[stack[-1]] < temperatures[i]:
                    temp = stack.pop()
                    output[temp] = i - temp
                stack.append(i)
        return output      