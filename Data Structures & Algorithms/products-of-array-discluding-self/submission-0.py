class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        if 0 in nums:
            mapping = Counter(nums)
            if mapping[0] > 1:
                return [0] * len(nums)
            index = 0
            for i in range(len(nums)):
                if nums[i] != 0:
                    product *= nums[i]
                else:
                    index = i
            l1 = [0] * len(nums)
            l1[index] = product
            return l1
        for i in range(len(nums)):
            product *= nums[i]
        output = []
        for j in range(len(nums)):
            output.append(product//nums[j])
        return output
        