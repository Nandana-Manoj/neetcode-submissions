class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for i in nums:
            freq[i] += 1

        sorted_dict = sorted(freq.items(), key = lambda item:item[1], reverse = True)

        return [i[0] for i in sorted_dict[:k]] 