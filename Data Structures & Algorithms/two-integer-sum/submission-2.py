class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res_dict = {}

        for idx, val in enumerate(nums):
            check = target - val
            if check not in res_dict:
                res_dict[val] = idx
            else:
                return [res_dict[check], idx]
