class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        running = 0
        longest = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                running += 1
                longest = max(running, longest)
            else:
                running = 0
        return longest
