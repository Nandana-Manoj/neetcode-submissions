class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = tuple(sorted(set(nums)))
        if len(nums) == 0:
            return 0

        longest = 1
        sub_long = 1


        for i in range(1, len(nums)):
            if nums[i-1] + 1 == nums[i]:
                sub_long += 1
                if sub_long > longest:
                    longest = sub_long

            else:
                sub_long = 1
        
        return longest
