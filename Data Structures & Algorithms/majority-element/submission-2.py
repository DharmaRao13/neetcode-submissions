import random

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n =len(nums)
        count = 0
        for num in nums:
            candidate = random.choice(nums)
            if nums.count(candidate) > n // 2:
                return candidate