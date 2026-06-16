class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        needed = []
        for i in range(len(nums)):
            num = nums[i]
            if num in needed:
                # print([needed.index(nums[i]), i])
                return [needed.index(num), i]
            needed.append(target-num)
            # print(needed)