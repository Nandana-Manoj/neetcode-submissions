class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        needed = []
        for i in range(len(nums)):
            if nums[i] in needed:
                # print([needed.index(nums[i]), i])
                return [needed.index(nums[i]), i]
            needed.append(target-nums[i])
            print(needed)