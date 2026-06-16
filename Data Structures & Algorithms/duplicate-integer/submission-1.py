class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = []
        for i in nums:
            if i in seen:
                return True
            seen.append(i)
        # print("None found")
        return False