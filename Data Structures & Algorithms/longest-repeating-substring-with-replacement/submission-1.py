class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int)
        highestFreq = 0
        l = 0
        maxLen = 0
        for r in range(len(s)):
            counter[s[r]] += 1
            highestFreq = max(counter[s[r]], highestFreq)
            while (r - l + 1 - highestFreq) > k:
                counter[s[l]] -= 1
                l += 1
            maxLen = max(r - l + 1, maxLen)
        
        return maxLen