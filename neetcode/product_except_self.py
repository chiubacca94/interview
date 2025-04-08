from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [1] * length
        
        prefix = 1
        for i in range(length):
            res[i] *= prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(length-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res

test = Solution()
nums = [1,2,3,4]
print(test.productExceptSelf(nums))
# Output: [24,12,8,6]