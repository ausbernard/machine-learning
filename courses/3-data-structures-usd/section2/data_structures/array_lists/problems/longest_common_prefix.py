from typing import List

class LongestPrefix:
    def longestCommonPrefix(self,strs: List[str]) -> str:
        if not strs or strs[0] == "":
            return ""
        
        
        # initialize i
        i = 0
        
        min_length = float('inf')
        for s in strs:
            if len(s) < min_length:
                min_length = len(s)
                
        while i < min_length:
            for s in strs:
                if s[i] != strs[0][i]:
                    return s[:i]
            i += 1
        
        return s[:i]
        

long_prefix = LongestPrefix()
output = long_prefix.longestCommonPrefix(["dog","racecar","car"])
print(output)

