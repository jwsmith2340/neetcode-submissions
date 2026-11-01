class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for val in strs:
            res += f"{len(val)};{val}"
        
        return res

    def decode(self, s: str) -> List[str]:
        # 2;we3;say1;:3;yes10;!@#$%^&*()"
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != ";":
                j += 1
            
            length = int(s[i:j])
            start = j + 1
            end = j + 1 + length
            res.append(s[start : end])

            i = end

        return res               
