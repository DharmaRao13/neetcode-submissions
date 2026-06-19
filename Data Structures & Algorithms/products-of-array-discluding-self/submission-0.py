class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n =len(nums)
        output = [0] * n
        for i in range(len(nums)):
            prod = 1
            for j in range(n):
                if j != i:
                    prod *= nums[j]
            output[i] = prod
        return output
