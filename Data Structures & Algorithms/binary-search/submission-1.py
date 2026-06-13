class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1

        while True:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif hi == lo or hi < 0 or lo > len(nums):
                return -1
            elif nums[mid] > target:
                hi = mid - 1
            elif nums[mid] < target:
                lo = mid + 1

        