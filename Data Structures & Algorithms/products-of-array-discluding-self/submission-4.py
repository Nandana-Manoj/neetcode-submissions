class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        num_zeros = sum(1 for num in nums if num == 0)
        if num_zeros > 1:
            return [0 for num in nums]

        if any(nums) != 0:        
            product = math.prod(num for num in nums if num != 0)
        else:
            product = 0
        
        if 0 in nums:
            ret = [0 if num != 0 else product for num in nums]
            return ret
        ret = [product // x for x in nums]

        return ret