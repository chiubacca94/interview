from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s
        
        return res

    # WATCH OUT FOR THIS: double digits
    def decode(self, s: str) -> List[str]:
        i = 0
        s_length = len(s)
        ans = []

        while i < s_length:
            # Check for double+ digit numbers
            j = i
            current_length = 0
            while s[j] != "#":
                j += 1  
            
            current_length = int(s[i:j])

            i = j + 1
            j = i + current_length

            substring = s[i:j]
            ans.append(substring)

            i = j

        return ans

test_input1 = ["neet","code","love","you"]
test_input2 = ["we","say",":","yes","!@#$%^&*()"]
test = Solution()
encoded = test.encode(test_input2)
print(encoded)
decoded = test.decode(encoded)
