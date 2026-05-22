class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, ele = 0, 0
        n = len(nums)
        
        for num in nums:
            if count == 0:
                count = 1
                ele = num
            elif ele == num:
                count += 1
            else:
                count -= 1
        
        cnt = nums.count(ele)
        if cnt > (n // 2):
            return ele
