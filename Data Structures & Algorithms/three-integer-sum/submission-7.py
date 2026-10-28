class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        outputList = []
        nums.sort()
        for outerIndex, num1 in enumerate(nums):
            if num1 > 0:
                break
            
            if outerIndex > 0 and num1 == nums[outerIndex - 1]:
                continue
            
            l = outerIndex + 1
            r = len(nums) - 1
            while l < r:
                potential = [num1, nums[l], nums[r]]
                if sum(potential) == 0:
                    outputList.append(potential)
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif sum(potential) > 0:
                    r -= 1
                else:
                    l += 1
        return outputList
                

        