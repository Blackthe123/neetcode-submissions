class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mapping = {}
        mapping2 = {}
        for i in range(len(s)):
            if s[i] not in mapping:
                mapping[s[i]] = 1
            else:
                mapping[s[i]] += 1
        for j in range(len(t)):
            if t[j] not in mapping2:
                mapping2[t[j]] = 1
            else:
                mapping2[t[j]] += 1
        return mapping == mapping2
