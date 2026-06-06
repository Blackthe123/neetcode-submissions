class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        l = [nums[i % len(nums)] for i in range(2*len(nums))]
        return l
