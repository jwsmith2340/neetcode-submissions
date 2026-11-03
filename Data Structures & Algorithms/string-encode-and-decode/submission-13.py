class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for val in strs:
            res += str(len(val)) + "#" + val
        
        return res

    def decode(self, s: str) -> List[str]:
        res_list = []
        i = 0
        # 5#Hello5#World
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            start = j + 1
            end = j + 1 + length
            res_list.append(s[start : end])
            i = end

        return res_list
