class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
            
        strs.sort()

        index = 0
        first = strs[0]
        last = strs[-1]

        while index < len(first) and index < len(last) and first[index] == last[index]:
            index += 1
        
        return first[:index]
