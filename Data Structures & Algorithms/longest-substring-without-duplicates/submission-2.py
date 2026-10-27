class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        distinctChar = set()
        l = 0
        globalMax = 0
        for char in s:
            if char in distinctChar:
                globalMax = max(len(distinctChar), globalMax)
                while s[l] != char:
                    distinctChar.remove(s[l])
                    l += 1
                if l != len(s) - 1:
                    l += 1
            else:
                distinctChar.add(char)
        
        globalMax = max(len(distinctChar), globalMax)
        return globalMax


        