class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_dict = dict()
        for i in range(len(strs)):
            sorted_dict[i] = "".join(sorted(strs[i]))
        grouped_dict = defaultdict(list)
        for key, value in sorted_dict.items():
            grouped_dict[value].append(key)

        final_list = []
        for k, v in grouped_dict.items():
            final_list.append([strs[i] for i in v])
        return final_list

