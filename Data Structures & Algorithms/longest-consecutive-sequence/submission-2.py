class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        print(nums, sorted(set(nums)))
        nums = tuple(sorted(set(nums)))

        if len(nums) == 0:
            return 0

        longest = 1
        sub_long = 1

        print(nums)

        for i in range(1, len(nums)):
            print("i-1:", nums[i-1], "i:", nums[i])
            if nums[i-1] + 1 == nums[i]:
                sub_long += 1
                if sub_long > longest:
                    longest = sub_long

                print("Sub:", sub_long, "Long:", longest)
            else:
                sub_long = 1
        
        return longest
