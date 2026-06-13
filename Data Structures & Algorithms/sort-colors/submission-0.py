class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p = 0
        for i in range(len(nums)):
            smallest = i
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[smallest]:
                    smallest = j
            nums[i], nums[smallest] = nums[smallest], nums[i]