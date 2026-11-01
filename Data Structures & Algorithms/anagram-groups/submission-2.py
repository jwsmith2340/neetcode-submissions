class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res_dict = {}
        res_list = []

        for val in strs:
            sorted_val = ''.join(sorted(val))
            if sorted_val not in res_dict:
                res_dict[sorted_val] = []
            res_dict[sorted_val].append(val)

        for val in res_dict.values():
            res_list.append(val)
        
        return res_list
   