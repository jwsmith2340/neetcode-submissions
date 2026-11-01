class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res_dict = {}
        res_list = []
        return_list = []

        for val in nums:
            if val not in res_dict:
                res_dict[val] = 0
            res_dict[val] += 1

        for key, val in res_dict.items():
            res_list.append((key, val))

        res_list.sort(key=lambda x: x[1], reverse=True)

        for idx in range(0, k):
            return_list.append(res_list[idx][0])

        return return_list
