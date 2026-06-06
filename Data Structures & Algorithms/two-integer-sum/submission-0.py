class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        potential = set()
        output = []
        for i in range(len(nums)):
            if nums[i] in potential:
                output.append(i)
                break
            potential.add(target - nums[i])
        for j in range(len(nums)):
            if nums[output[0]] + nums[j] == target:
                output.append(j)
                break
        output.sort()
        return output

        